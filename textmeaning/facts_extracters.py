import xmltodict
import subprocess
from os import path


class TomitaExtracter(object):
    def __init__(self, tomita_env='./tomita',
                        tomita_bin='tomita-linux64',
                        tomita_cfg='config.proto'):
        self.bin = tomita_bin
        self.cfg = tomita_cfg
        self.env = tomita_env

    def extract(self, raw_text="", fact_types=[]):
        cmpl_proc = subprocess.run([self.bin, self.cfg], input=raw_text,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                shell=False,
                                cwd=self.env,
                                encoding='utf8')
        dict_data = xmltodict.parse(cmpl_proc.stdout)['fdo_objects']['document']['facts']
        ftypes_dict = {}
        for f_type in fact_types:
            if f_type.__name__ not in dict_data:
                continue
    
            suitable_facts = dict_data[f_type.__name__]
            if type(suitable_facts) is not list:
                suitable_facts = list(suitable_facts)
            res = []
            for xml_fact in suitable_facts:
                fact = f_type()
                fact.from_dict(xml_fact, field_key='@val')
                res.append(fact)

            ftypes_dict[f_type.__name__] = res            
        return ftypes_dict
