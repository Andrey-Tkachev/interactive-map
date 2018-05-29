import xmltodict
import subprocess
from .facttypes import AdressFact
from typing import List, Dict
from os import path


class TomitaExtracter(object):
    def __init__(self, tomita_env='./tomita',
                        tomita_bin='tomita-linux64',
                        tomita_cfg='config.proto'):
        self.bin = tomita_bin
        self.cfg = tomita_cfg
        self.env = tomita_env

    def extract(self, raw_text: str, facttypes_to_extract: List[AdressFact]):
        cmpl_proc = subprocess.run([self.bin, self.cfg], input=raw_text.encode('utf-8'),
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                shell=False,
                                cwd=self.env)
        parsed_res = xmltodict.parse(cmpl_proc.stdout)
        if not parsed_res['fdo_objects']:
            return []
        dict_data = parsed_res['fdo_objects']['document']['facts']
        result_facts = []

        for facttype in facttypes_to_extract:
            if facttype.__name__ not in dict_data:
                continue
    
            suitable_facts = dict_data[facttype.__name__]
            if type(suitable_facts) is not list:
                suitable_facts = [suitable_facts]
            facts_of_curr_type = []
            for xml_fact in suitable_facts:
                fact = facttype()
                fact.from_dict(xml_fact, field_key='@val')
                facts_of_curr_type.append(fact)

            result_facts.extend(facts_of_curr_type)
        return result_facts
