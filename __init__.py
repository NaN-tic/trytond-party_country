#This file is part party_country module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.pool import Pool
from .configuration import *
from .address import *

def register():
    Pool.register(
        Configuration,
        Address,
        module='party_country', type_='model')
