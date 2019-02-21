# -*- coding: utf-8 -*-
# @Author  : itswcg
# @File    : forms.py
# @Time    : 19-2-20 下午9:55
# @Blog    : https://blog.itswcg.com
# @github  : https://github.com/itswcg

from django import forms


class AddressForm(forms.Form):
    address = forms.CharField()
