# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# See the COPYING file for license information.
#
# Copyright (c) 2011,2012 peo3 <peo314159265@gmail.com>
import sys
import os
import os.path
import re
import struct
import errno

from cgutils import host
from cgutils import process
from cgutils import fileops


if sys.version_info.major == 3:
    long = int


class SubsystemStatus(dict):
    __RE = '^(?P<name>\w+)\s+(?P<hier>\d+)\s+(?P<n>\d+)\s+(?P<enabled>[01])'
    _RE_CGROUPS = re.compile(__RE)

    def __init__(self):
        dict.__init__(self)
        self.paths = {}
        self.update()

    def _parse_proc_cgroups(self):
        """Parse /proc/cgroups"""

        """
        #subsys_name	hierarchy	num_cgroups	enabled
        cpuset	0	1	1
        ns	0	1	1
        cpu	1	10	1
        cpuacct	0	1	1
        memory	0	1	1
        devices	0	1	1
        freezer	0	1	1
        net_cls	0	1	1
        """
        for line in fileops.readlines('/proc/cgroups'):
            m = self._RE_CGROUPS.match(line)
            if m is None:
                continue

            name = m.group('name')
            hierarchy = int(m.group('hier'))
            n_cgroups = int(m.group('n'))
            if m.group('enabled') == '1':
                enabled = True
            else:
                enabled = False
            if name not in self:
                self[name] = {}
            self[name]['name'] = name
            self[name]['hierarchy'] = hierarchy
            self[name]['num_cgroups'] = n_cgroups
            self[name]['enabled'] = enabled

    def _parse_proc_mount(self):
        """Parse /proc/mounts"""

        """
        cgroup /cgroup/cpu cgroup rw,relatime,cpuacct,cpu,release_agent=/sbin/cgroup_clean 0 0
        cgroup /cgroup/memory cgroup rw,relatime,memory 0 0
        cgroup /cgroup/blkio cgroup rw,relatime,blkio 0 0
        cgroup /cgroup/freezer cgroup rw,relatime,freezer 0 0
        """

        for line in fileops.readlines('/proc/mounts'):
            if 'cgroup' not in line:
                continue

            items = line.split(' ')
            path = items[1]
            opts = items[3].split(',')

            name = None
            for opt in opts:
                if opt in self:
                    name = opt
                    self.paths[name] = path
                if 'name=' in opt:
                    # We treat name=XXX as its name
                    name = opt
                    self.paths[name] = path
                    self[name] = {}
                    self[name]['name'] = name
                    self[name]['enabled'] = True
                    self[name]['hierarchy'] = 0
                    self[name]['num_cgroups'] = 0
            # release_agent= may appear before name=
            for opt in opts:
                if 'release_agent=' in opt:
                    self[name]['release_agent'] = opt.replace('release_agent=', '')

    def _update(self):
        self._parse_proc_cgroups()
        self._parse_proc_mount()

    def update(self):
        self.clear()
        self._update()

    def get_all(self):
        return list(self.keys())

    def get_available(self):
        return [name for name in list(self.keys())
                if self[name]['enabled']]

    def get_enabled(self):
        return list(self.paths.keys())

    def get_path(self, subsys):
        return self.paths[subsys]


class SimpleList(list):
    @staticmethod
    def parse(content):
        ret = []
        for line in content.split('\n')[:-1]:
            ret.append(long(line))
        return ret


class SimpleStat(dict):
    @staticmethod
    def parse(content):
        ret = {}
        for line in content.split('\n')[:-1]:
            name, val = line.split(' ')
            ret[name] = long(val)
        return ret


class BlkioStat(dict):
    @staticmethod
    def parse(content):
        ret = {}
        for line in content.split('\n')[:-1]:
            if line.count(' ') == 2:
                dev, type, val = line.split(' ')
                if dev not in ret:
                    ret[dev] = {}
                ret[dev][type] = long(val)
            elif line.count(' ') == 1:
                type, val = line.split(' ')
                ret[type] = long(val)
            else:
                raise EnvironmentError(line)
        return ret


class DevicesStat(list):
    @staticmethod
    def parse(content):
        return [v for v in content.split('\n')[:-1] if v]


class NumaStat(dict):
    @staticmethod
    def parse(content):
        ret = {}
        lines = content.split('\n')[:-1]
        for line in lines:
            item = {}
            entries = line.split(' ')
            name, value = entries[0].split('=')
            item['total'] = long(value)
            for entry in entries[1:]:
                node, value = entry.split('=')
                item[node] = long(value)
            ret[name] = item
        return ret


class PercpuStat(dict):
    @staticmethod
    def parse(content):
        ret = {}
        line = content.split('\n')[0]
        stats = line.split(' ')
        # A line may end with a redundant space
        stats = [stat for stat in stats if stat != '']
        i = 0
        for stat in stats:
            ret[i] = long(stat)
            i += 1
        return ret


class CpuacctUsageAllStat(dict):
    @staticmethod
    def parse(content):
        # cpu user system
        # 0 26703258962 1612927964
        # 1 37879159293 1963003474

        ret = {}
        lines = content.split('\n')
        header = lines.pop(0)
        if header != "cpu user system":
            raise EnvironmentError("Invalid header: %s" % header)
        lines.remove('')

        for line in lines:
            cpuid, user, system = line.split(' ')
            ret[int(cpuid)] = (long(user), long(system))
        return ret


class SlabinfoStat(dict):
    def __parse_version_2_1(lines):
        # Drop legend '# name            <active_objs> <num_objs> <objsize> <objperslab> <pagesperslab> : tunables <limit> <batchcount> <sharedfactor> : slabdata <active_slabs> <num_slabs> <sharedavail>'
        lines.pop(0)

        # eg 'kmalloc-128           32     32    128   32    1 : tunables    0    0    0 : slabdata      1      1      0'
        r1 = re.compile('([\w\-\_]+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)')
        r2 = re.compile('tunables\s+(\d+)\s+(\d+)\s+(\d+)')
        r3 = re.compile('slabdata\s+(\d+)\s+(\d+)\s+(\d+)')

        ret = {}
        for line in lines:
            fields = [field.strip() for field in line.split(':')]

            # eg 'kmalloc-128           32     32    128   32    1'
            m = r1.match(fields[0])
            if not m:
                continue
            name = m.group(1)
            ret[name] = {
                'active_objs': long(m.group(2)),
                'num_objs': long(m.group(3)),
                'objsize': long(m.group(4)),
                'objperslab': long(m.group(5)),
                'pagesperslab': long(m.group(6)),
            }
            item = ret[name]

            # eg 'tunables    0    0    0'
            m = r2.match(fields[1])
            if not m:
                continue
            item['tunables'] = {
                'limit': long(m.group(1)),
                'batchcount': long(m.group(2)),
                'sharedfactor': long(m.group(3)),
            }

            # eg 'slabdata      1      1      0'
            m = r3.match(fields[2])
            if not m:
                continue
            item['slabdata'] = {
                'active_slabs': long(m.group(1)),
                'num_slabs': long(m.group(2)),
                'sharedavail': long(m.group(3)),
            }

        return ret

    _PARSERS = {
        '2.1': __parse_version_2_1,
    }

    @staticmethod
    def parse(content):
        lines = content.split('\n')
        # eg 'slabinfo - version: 2.1'
        header = lines.pop(0)
        m = re.match('slabinfo - version: ([\d\.]+)', header)
        if m:
            return SlabinfoStat._PARSERS[m.group(1)](lines)
        else:
            return None


class PidsEventsStat(dict):
    @staticmethod
    def parse(content):
        ret = {}
        lines = content.split('\n')
        lines.remove('')
        for line in lines:
            name, val = line.split(' ')
            ret[name] = long(val)
        return ret


class RdmaStat(dict):
    __RE = '^(?P<name>\w+)\s+hca_handle=(?P<hca_handle>\d+)\s+hca_object=(?P<hca_object>(\d+|max))'
    _RE = re.compile(__RE)

    @staticmethod
    def parse(content):
        """ Parse rdma.curren and rdma.max

        Example contents:
          mlx4_0 hca_handle=2 hca_object=2000
          ocrdma1 hca_handle=3 hca_object=max

        >>> RdmaStat.parse("mlx4_0 hca_handle=2 hca_object=2000\\nocrdma1 hca_handle=3 hca_object=max")
        {'mlx4_0': {'hca_handle': 2, 'hca_object': 2000}, 'ocrdma1': {'hca_handle': 3, 'hca_object': 'max'}}
        """
        ret = {}
        lines = content.split('\n')
        for line in lines:
            m = RdmaStat._RE.match(line)
            if m is None:
                continue
            name = m.group('name')
            hca_handle = long(m.group('hca_handle'))
            hca_object = m.group('hca_object')
            if hca_object != "max":
                hca_object = long(hca_object)
            ret[name] = {"hca_handle": hca_handle, "hca_object": hca_object}
        return ret


#
# The base class of subsystems
#
class Subsystem(object):
    CONFIGS = {}
    STATS = {}
    CONTROLS = {}
    NAME = None

    def __init__(self):
        self.name = self.NAME

    def get_init_parameters(self, parent_configs):
        return {}


#
# Classes of each subsystem
#
class SubsystemCpu(Subsystem):
    NAME = 'cpu'
    _path_rt_period = '/proc/sys/kernel/sched_rt_period_us'
    _path_rt_runtime = '/proc/sys/kernel/sched_rt_runtime_us'
    STATS = {
        'stat': SimpleStat,
    }
    CONFIGS = {
        'shares':        1024,
        # Are the default values correct?
        'rt_period_us':  long(fileops.read(_path_rt_period)),
        'rt_runtime_us': long(fileops.read(_path_rt_runtime)),
        'cfs_period_us': 100000,
        'cfs_quota_us': -1,
    }


class SubsystemCpuacct(Subsystem):
    NAME = 'cpuacct'
    STATS = {
        'usage': long,
        'stat': SimpleStat,
        'usage_all': CpuacctUsageAllStat,
        'usage_sys':  long,
        'usage_user': long,
        'usage_percpu':      PercpuStat,
        'usage_percpu_sys':  PercpuStat,
        'usage_percpu_user': PercpuStat,
    }


class SubsystemCpuset(Subsystem):
    NAME = 'cpuset'
    STATS = {
        # str object something like '0', '0-1', and '0-1,3,4'
        'effective_cpus': str,
        'effective_mems': str,
        'memory_pressure': long,
    }
    CONFIGS = {
        'cpu_exclusive': 0,
        # same as 'effective_*' ones
        'cpus': host.CPUInfo().get_online(),
        'mem_exclusive': 0,
        'mem_hardwall': 0,
        'memory_migrate': 0,
        'memory_pressure_enabled': 0,
        'memory_spread_page': 0,
        'memory_spread_slab': 0,
        # same as 'cpus'
        'mems': host.MemInfo().get_online(),
        'sched_load_balance': 1,
        'sched_relax_domain_level': -1,
    }

    def get_init_parameters(self, parent_configs):
        params = {}
        params['cpus'] = parent_configs['cpus']
        params['mems'] = parent_configs['mems']
        return params


class SubsystemMemory(Subsystem):
    NAME = 'memory'
    STATS = {
        'failcnt': long,
        'usage_in_bytes': long,
        'max_usage_in_bytes': long,
        'memsw.failcnt': long,
        'memsw.max_usage_in_bytes': long,
        'memsw.usage_in_bytes': long,
        'stat': SimpleStat,
        'numa_stat': NumaStat,
        'kmem.tcp.failcnt': long,
        'kmem.tcp.max_usage_in_bytes': long,
        'kmem.tcp.usage_in_bytes': long,
        'kmem.failcnt': long,
        'kmem.max_usage_in_bytes': long,
        'kmem.usage_in_bytes': long,
        'kmem.slabinfo': SlabinfoStat,
    }
    MAX_ULONGLONG = 2 ** 63 - 1
    CONFIGS = {
        'limit_in_bytes': MAX_ULONGLONG,
        'memsw.limit_in_bytes': MAX_ULONGLONG,
        'move_charge_at_immigrate': 0,
        'oom_control': SimpleStat({'oom_kill_disable': 0, 'under_oom': 0}),
        'soft_limit_in_bytes': MAX_ULONGLONG,
        'swappiness': 60,
        'use_hierarchy': 0,
        'kmem.tcp.limit_in_bytes': MAX_ULONGLONG,
        'kmem.limit_in_bytes': MAX_ULONGLONG,
    }
    CONTROLS = {
        'force_empty': None,
        'pressure_level': None,
    }


class SubsystemBlkio(Subsystem):
    NAME = 'blkio'
    STATS = {
        'io_merged': BlkioStat,
        'io_merged_recursive': BlkioStat,
        'io_queued': BlkioStat,
        'io_queued_recursive': BlkioStat,
        'io_service_bytes': BlkioStat,
        'io_service_bytes_recursive': BlkioStat,
        'io_service_time': BlkioStat,
        'io_service_time_recursive': BlkioStat,
        'io_serviced': BlkioStat,
        'io_serviced_recursive': BlkioStat,
        'io_wait_time': BlkioStat,
        'io_wait_time_recursive': BlkioStat,
        'sectors': SimpleStat,
        'sectors_recursive': SimpleStat,
        'throttle.io_service_bytes': BlkioStat,
        'throttle.io_serviced': BlkioStat,
        'throttle.io_service_bytes_recursive': BlkioStat,
        'throttle.io_serviced_recursive': BlkioStat,
        'time': SimpleStat,
        'time_recursive': SimpleStat,
        # Debugging files (Appeared only CONFIG_DEBUG_BLK_CGROUP=y)
        'avg_queue_size': BlkioStat,
        'dequeue': BlkioStat,
        'empty_time': BlkioStat,
        'group_wait_time': BlkioStat,
        'idle_time': BlkioStat,
        'unaccounted_time': BlkioStat,
    }
    CONFIGS = {
        'leaf_weight': 1000,
        'leaf_weight_device': SimpleStat({}),
        'throttle.read_iops_device': SimpleStat({}),
        'throttle.write_iops_device': SimpleStat({}),
        'throttle.read_bps_device': SimpleStat({}),
        'throttle.write_bps_device': SimpleStat({}),
        'weight': 1000,
        'weight_device': SimpleStat({}),
    }
    CONTROLS = {
        'reset_stats': None,
    }


class SubsystemFreezer(Subsystem):
    NAME = 'freezer'
    STATS = {
        'state': str,
        'parent_freezing': long,
        'self_freezing': long,
    }


class SubsystemNetCls(Subsystem):
    NAME = 'net_cls'
    CONFIGS = {
        'classid': 0,
    }


class SubsystemDevices(Subsystem):
    NAME = 'devices'
    CONFIGS = {
        'list': DevicesStat(['a *:* rwm']),
    }
    CONTROLS = {
        'allow': None,
        'deny': None,
    }


class SubsystemNetPrio(Subsystem):
    NAME = 'net_prio'
    STATS = {
        'prioidx': long,
    }
    __ifs = os.listdir('/sys/class/net')
    CONFIGS = {
        'ifpriomap': SimpleStat(list(zip(__ifs, [0] * len(__ifs)))),
    }


class SubsystemHugetlb(Subsystem):
    NAME = 'hugetlb'
    MAX_ULONGLONG = 2 ** 63 - 1
    # FIXME: this is x86 specific and we have to treat
    # different size of HugeTLB on other architectures.
    __stats = {}
    __configs = {}
    for __size in ('2MB', '1GB'):
        __stats.update({
            __size + '.failcnt': long,
            __size + '.max_usage_in_bytes': long,
            __size + '.usage_in_bytes': long,
        })
        __configs.update({
            __size + '.limit_in_bytes': MAX_ULONGLONG,
        })
    STATS = __stats
    CONFIGS = __configs


class SubsystemPids(Subsystem):
    NAME = 'pids'
    STATS = {
        'current': long,
        'events': PidsEventsStat,
    }
    CONFIGS = {
        'max': 'max',
    }


class SubsystemRdma(Subsystem):
    NAME = 'rdma'
    STATS = {
        'current': RdmaStat,
    }
    CONFIGS = {
        'max': RdmaStat,
    }


class SubsystemName(Subsystem):
    NAME = 'name'

    def __init__(self, name):
        Subsystem.__init__(self)
        self.name = name


_subsystem_name2class = {
    'cpu': SubsystemCpu,
    'cpuacct': SubsystemCpuacct,
    'cpuset': SubsystemCpuset,
    'memory': SubsystemMemory,
    'blkio': SubsystemBlkio,
    'freezer': SubsystemFreezer,
    'net_cls': SubsystemNetCls,
    'devices': SubsystemDevices,
    'net_prio': SubsystemNetPrio,
    'hugetlb': SubsystemHugetlb,
    'pids': SubsystemPids,
    'rdma': SubsystemRdma,
}


def _get_subsystem(name):
    if 'name=' in name:
        return SubsystemName(name)
    return _subsystem_name2class[name]()


class NoSuchControlFileError(Exception):
    pass


class IsRootGroupError(Exception):
    pass


class CGroup:
    """
    This class represents a control group in a cgroup hierarchy.

    An instance belongs to a paticluar subsystem, thus, only one
    file path is determined to the instance.

    An instance has control files of both a cgroup and a subsystem
    which the instance belongs to. An instance can have child
    cgroups under the cgroup directory of the instace.

    The class categorises control files into three groups: configs
    include configurable files, stats include statistics of the
    group, and controls include special configuration files which
    are normally write-only.
    """
    _STATS = {
        'tasks': SimpleList,
        'cgroup.procs': SimpleList,
    }
    _CONFIGS = {
        'release_agent': '',
        # XXX: the default value is actually inherited from a parent
        'notify_on_release': 0,
        'cgroup.clone_children': 0,
    }
    _CONTROLS = {
        'cgroup.event_control': None,
    }
    _PARSERS = {
        int: lambda content: int(content),
        long: lambda content: long(content),
        str: lambda content: content.strip(),
        SimpleList: SimpleList.parse,
        SimpleStat: SimpleStat.parse,
        BlkioStat: BlkioStat.parse,
        DevicesStat: DevicesStat.parse,
        NumaStat: NumaStat.parse,
        PercpuStat: PercpuStat.parse,
        SlabinfoStat: SlabinfoStat.parse,
        CpuacctUsageAllStat: CpuacctUsageAllStat.parse,
        PidsEventsStat: PidsEventsStat.parse,
        RdmaStat: RdmaStat.parse,
    }

    def _calc_depth(self, path):
        def rec(path):
            rest = os.path.split(path)[0]
            if rest == '/':
                return 1
            else:
                return rec(rest) + 1
        return rec(path)

    def __init__(self, subsystem, fullpath, parent=None, filters=list()):
        self.subsystem = subsystem
        self.fullpath = fullpath
        self.parent = parent
        self.filters = filters

        status = SubsystemStatus()
        mount_point = status.get_path(subsystem.name)
        path = fullpath.replace(mount_point, '')
        self.path = '/' if path == '' else path

        if self.path == '/':
            self.depth = 0
            self.fullname = self.name = '/'
        else:
            self.depth = self._calc_depth(self.path)
            self.name = os.path.basename(self.path)
            self.fullname = self.path[1:]

        if self.parent is None and self.depth != 0:
            # XXX: We should do out of the class?
            self.parent = get_cgroup(os.path.dirname(self.fullpath))

        self.paths = {}
        for file in list(self._STATS.keys()) + list(self._CONFIGS.keys()) + list(self._CONTROLS.keys()):
            self.paths[file] = os.path.join(self.fullpath, file)
        for file in list(subsystem.STATS.keys()) + list(subsystem.CONFIGS.keys()) + list(subsystem.CONTROLS.keys()):
            self.paths[file] = os.path.join(self.fullpath, subsystem.name + '.' + file)

        self.configs = {}
        self.configs.update(self._CONFIGS)
        self.configs.update(subsystem.CONFIGS)
        self.stats = {}
        self.stats.update(self._STATS)
        self.stats.update(subsystem.STATS)
        if self.filters:
            self.apply_filters(filters)

        self.childs = []
        self.pids = []
        self.n_procs = 0

        self.update()

    def __str__(self):
        return "<CGroup: %s (%s)>" % (self.fullname, self.subsystem.name)

    def __hash__(self):
        return hash((self.fullname, self.subsystem.name))

    def __eq__(self, obj):
        return self.fullname == obj.fullname and self.subsystem.name == obj.subsystem.name

    def apply_filters(self, filters):
        """
        It applies a specified filters. The filters are used to reduce the control groups
        which are accessed by get_confgs, get_stats, and get_defaults methods.
        """
        _configs = self.configs
        _stats = self.stats
        self.configs = {}
        self.stats = {}
        for f in filters:
            if f in _configs:
                self.configs[f] = _configs[f]
            elif f in _stats:
                self.stats[f] = _stats[f]
            else:
                raise NoSuchControlFileError("%s for %s" % (f, self.subsystem.name))

    def get_configs(self):
        """
        It returns a name and a current value pairs of control files
        which are categorised in the configs group.
        """
        configs = {}
        for name, default in self.configs.items():
            cls = default.__class__
            path = self.paths[name]
            if os.path.exists(path):
                try:
                    configs[name] = self._PARSERS[cls](fileops.read(path))
                except IOError as e:
                    if e.errno == errno.EOPNOTSUPP:
                        # Since 3.5 memory.memsw.* are always created even if disabled.
                        # If disabled we will get EOPNOTSUPP when read or write them.
                        # See commit af36f906c0f4c2ffa0482ecdf856a33dc88ae8c5 of the kernel.
                        pass
                    else:
                        raise
        return configs

    def get_default_configs(self):
        """
        It is similar to get_configs but it returns default values
        instead of current values.
        """
        return self.configs.copy()

    def get_stats(self):
        """
        It returns a name and a value pairs of control files
        which are categorised in the stats group.
        """
        stats = {}
        for name, cls in self.stats.items():
            path = self.paths[name]
            if os.path.exists(path):
                try:
                    stats[name] = self._PARSERS[cls](fileops.read(path))
                except IOError as e:
                    # XXX: we have to distinguish unexpected errors from the expected ones
                    if e.errno == errno.EOPNOTSUPP:
                        # Since 3.5 memory.memsw.* are always created even if disabled.
                        # If disabled we will get EOPNOTSUPP when read or write them.
                        # See commit af36f906c0f4c2ffa0482ecdf856a33dc88ae8c5 of the kernel.
                        pass
                    if e.errno == errno.EIO:
                        # memory.kmem.slabinfo throws EIO until limit_in_bytes is set.
                        pass
                    else:
                        raise
        return stats

    def update(self):
        """It updates process information of the cgroup."""
        pids = fileops.readlines(self.paths['cgroup.procs'])
        self.pids = [int(pid) for pid in pids if pid != '']
        self.n_procs = len(pids)

    def set_config(self, name, value):
        path = os.path.join(self.fullpath, self.subsystem.name + '.' + name)
        fileops.write(path, str(value))

    def mkdir(self, name, set_initparams=True):
        new_path = os.path.join(self.fullpath, name)
        fileops.mkdir(new_path)
        new = get_cgroup(new_path)
        if set_initparams:
            params = self.subsystem.get_init_parameters(self.get_configs())
            for filename, value in params.items():
                new.set_config(filename, value)
        return new

    def rmdir(self, target=None):
        if self.depth == 0:
            raise IsRootGroupError("%s is a root cgroup" % self.fullpath)

        if target:
            if not isinstance(target, CGroup):
                raise TypeError('Not a CGroup instance')
        else:
            target = self.parent

        self.update()

        for pid in self.pids:
            target.attach(pid)
        fileops.rmdir(self.fullpath)

    def attach(self, pid):
        if not process.exists(pid):
            raise EnvironmentError("Process %d not exists" % pid)

        fileops.write(self.paths['tasks'], str(pid))


class EventListener:
    """
    It enable us to use event notification feature of control groups.

    To use this feature, we have to specify a cgroup
    and a target control file of the cgroup.
    """
    SUPPORTED_FILES = [
        'memory.usage_in_bytes',
        'memory.oom_control',
        'memory.memsw.usage_in_bytes',
        'memory.pressure_level',
    ]

    def __init__(self, cgroup, target_name):
        from cgutils import linux

        self.cgroup = cgroup
        self.target_name = target_name

        if target_name not in self.SUPPORTED_FILES:
            raise EnvironmentError("%s is not supported by the kernel" % target_name)

        target_path = os.path.join(cgroup.fullpath, target_name)

        # To keep the files open, set them in instance variables
        self.target_file = open(target_path)
        self.target_fd = self.target_file.fileno()

        ec_path = self.cgroup.paths['cgroup.event_control']
        self.ec_file = open(ec_path, 'w')
        self.ec_fd = self.ec_file.fileno()

        self.event_fd = linux.eventfd(0, 0)

    def register(self, arguments=list()):
        """
        Register a target file with arguments (if required) to a event_control file
        which we want to be notified events.
        """
        target_name = self.target_name
        if target_name in ['memory.usage_in_bytes', 'memory.memsw.usage_in_bytes']:
            threshold = arguments[0]
            line = "%d %d %d\0" % (self.event_fd, self.target_fd, long(threshold))
        elif target_name in ['memory.pressure_level']:
            threshold = arguments[0]
            line = "%d %d %s\0" % (self.event_fd, self.target_fd, threshold)
        else:
            line = "%d %d\0" % (self.event_fd, self.target_fd)
        os.write(self.ec_fd, line)

    def wait(self):
        """
        It returns when an event which we have configured by set_threshold happens.
        Note that it blocks until then.
        """
        ret = os.read(self.event_fd, 64 / 8)
        return struct.unpack('Q', ret)


def _scan_cgroups_recursive(subsystem, fullpath, mount_point, filters):
    cgroup = CGroup(subsystem, fullpath=fullpath, filters=filters)

    _childs = []
    for _file in os.listdir(fullpath):
        child_fullpath = os.path.join(fullpath, _file)
        if os.path.isdir(child_fullpath):
            child = _scan_cgroups_recursive(subsystem, child_fullpath,
                                            mount_point, filters)
            _childs.append(child)
    cgroup.childs.extend(_childs)
    return cgroup


#
#  Public APIs
#
class NoSuchSubsystemError(Exception):
    pass


def scan_cgroups(subsys_name, filters=list()):
    """
    It returns a control group hierarchy which belong to the subsys_name.
    When collecting cgroups, filters are applied to the cgroups. See pydoc
    of apply_filters method of CGroup for more information about the filters.
    """
    status = SubsystemStatus()
    if subsys_name not in status.get_all():
        raise NoSuchSubsystemError("No such subsystem found: " + subsys_name)

    if subsys_name not in status.get_available():
        raise EnvironmentError("Disabled in the kernel: " + subsys_name)

    if subsys_name not in status.get_enabled():
        raise EnvironmentError("Not enabled in the system: " + subsys_name)

    subsystem = _get_subsystem(subsys_name)
    mount_point = status.get_path(subsys_name)
    return _scan_cgroups_recursive(subsystem, mount_point, mount_point, filters)


def walk_cgroups(cgroup, action, opaque):
    """
    The function applies the action function with the opaque object
    to each control group under the cgroup recursively.
    """
    action(cgroup, opaque)
    for child in cgroup.childs:
        walk_cgroups(child, action, opaque)


def get_cgroup(fullpath):
    """
    It returns a CGroup object which is pointed by the fullpath.
    """
    # Canonicalize symbolic links
    fullpath = os.path.realpath(fullpath)

    status = SubsystemStatus()
    name = None
    for name, path in status.paths.items():
        if path in fullpath:
            break
    else:
        raise Exception('Invalid path: ' + fullpath)
    subsys = _get_subsystem(name)

    return CGroup(subsys, fullpath)
