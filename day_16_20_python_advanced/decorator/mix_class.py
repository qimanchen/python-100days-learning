#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class SetOnceMappingMixin():
    """自定义混入类"""
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)


class SetOnceDict(SetOnceMappingMixin, dict):
    """自定义字典"""
    pass


my_dict= SetOnceDict()
try:
	# 只有当字典中不存在相应的key时才可对key赋予相应的value
    my_dict['username'] = 'jackfrued'
    my_dict['username'] = 'hellokitty'
except KeyError:
    pass
print(my_dict) #{'username':'jackfrued'}