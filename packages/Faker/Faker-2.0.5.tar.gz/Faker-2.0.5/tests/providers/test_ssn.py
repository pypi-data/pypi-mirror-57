#  -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re
import unittest
from datetime import datetime
from itertools import cycle

import freezegun
import pytest
import random2
from validators.i18n.es import es_cif as is_cif, es_nif as is_nif, es_nie as is_nie

from faker import Faker
from faker.providers.ssn.en_CA import checksum as ca_checksum
from faker.providers.ssn.et_EE import checksum as et_checksum
from faker.providers.ssn.fi_FI import Provider as fi_Provider
from faker.providers.ssn.hr_HR import checksum as hr_checksum
from faker.providers.ssn.no_NO import checksum as no_checksum, Provider as no_Provider
from faker.providers.ssn.pl_PL import checksum as pl_checksum, calculate_month as pl_calculate_mouth
from faker.providers.ssn.pt_BR import checksum as pt_checksum
from faker.providers.ssn.es_MX import (ssn_checksum as mx_ssn_checksum,
                                       curp_checksum as mx_curp_checksum)


class TestSvSE(unittest.TestCase):
    def setUp(self):
        self.factory = Faker('sv_SE')

    def partial_sum(self, number, mult_factor):
        quotient, remainder = divmod(number * mult_factor, 10)
        return quotient + remainder

    def ssn_checksum(self, ssn):
        """Validates the checksum digit and returns a Boolean"""
        ssn = ssn.replace('-', '')
        if len(ssn) == 12:
            ssn = ssn[2:]
        if len(ssn) != 10:
            return False

        mult_factors = cycle([2, 1])
        final_sum = sum(self.partial_sum(int(char), mf) for char, mf in zip(ssn[:9], mult_factors))
        chksum = -final_sum % 10
        return chksum == int(ssn[-1])

    def validate_date_string(self, date_str):
        date_len = len(date_str)
        if date_len == 6:
            year_fmt = '%y'
        elif date_len == 8:
            year_fmt = '%Y'
        else:
            return False

        try:
            if date_str != datetime.strptime(date_str, '{}%m%d'.format(year_fmt)).strftime('{}%m%d'.format(year_fmt)):
                raise ValueError
            return True
        except ValueError:
            return False

    def test_pers_id_short_with_dash(self):
        """Regression case that ensures previous implementations work as-is"""
        for _ in range(100):
            pers_id = self.factory.ssn()
            assert re.search(r'\d{6}-\d{4}', pers_id)
            assert self.validate_date_string(pers_id[:6]) is True
            assert self.ssn_checksum(pers_id) is True

    def test_pers_id_short_no_dash(self):
        for _ in range(100):
            pers_id = self.factory.ssn(dash=False)
            assert re.search(r'\d{10}', pers_id)
            assert self.validate_date_string(pers_id[:6]) is True
            assert self.ssn_checksum(pers_id) is True

    def test_pers_id_long_with_dash(self):
        for _ in range(100):
            pers_id = self.factory.ssn(long=True)
            assert re.search(r'\d{8}-\d{4}', pers_id)
            assert self.validate_date_string(pers_id[:8]) is True
            assert self.ssn_checksum(pers_id) is True

    def test_pers_id_long_no_dash(self):
        for _ in range(100):
            pers_id = self.factory.ssn(long=True, dash=False)
            assert re.search(r'\d{12}', pers_id)
            assert self.validate_date_string(pers_id[:8]) is True
            assert self.ssn_checksum(pers_id) is True

    def test_org_id_short_with_dash(self):
        for _ in range(100):
            org_id = self.factory.org_id()
            assert re.search(r'\d{6}-\d{4}', org_id)
            assert int(org_id[2:4]) >= 20
            assert self.ssn_checksum(org_id) is True

    def test_org_id_short_no_dash(self):
        for _ in range(100):
            org_id = self.factory.org_id(dash=False)
            assert re.search(r'\d{10}', org_id)
            assert int(org_id[2:4]) >= 20
            assert self.ssn_checksum(org_id) is True

    def test_org_id_long_with_dash(self):
        for _ in range(100):
            org_id = self.factory.org_id(long=True)
            assert re.search(r'\d{8}-\d{4}', org_id)
            assert int(org_id[4:6]) >= 20
            assert self.ssn_checksum(org_id) is True

    def test_org_id_long_no_dash(self):
        for _ in range(100):
            org_id = self.factory.org_id(long=True, dash=False)
            assert re.search(r'\d{12}', org_id)
            assert int(org_id[4:6]) >= 20
            assert self.ssn_checksum(org_id) is True

    def test_vat_id(self):
        for _ in range(100):
            vat_id = self.factory.vat_id()
            assert re.search(r'SE\d{12}', vat_id)
            assert int(vat_id[2]) in (1, 2, 3, 5, 6, 7, 8, 9)
            assert int(vat_id[6:8]) >= 20

    def test_org_and_vat_id(self):
        for _ in range(100):
            oid, vid = self.factory.org_and_vat_id()
            assert oid.replace('-', '')[-10:] == vid[4:-2]
            assert re.search(r'SE\d{12}', vid)


class TestBgBG(unittest.TestCase):
    def setUp(self):
        self.factory = Faker('bg_BG')

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r'^BG\d{9,10}$', self.factory.vat_id())


class TestCsCZ(unittest.TestCase):
    def setUp(self):
        self.factory = Faker('cs_CZ')

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r'^CZ\d{8,10}$', self.factory.vat_id())


class TestDeAT(unittest.TestCase):
    def setUp(self):
        self.factory = Faker('de_AT')

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r'^ATU\d{8}$', self.factory.vat_id())


class TestElCY(unittest.TestCase):
    def setUp(self):
        self.factory = Faker('el_CY')

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r'^CY\d{9}\w$', self.factory.vat_id())


class TestElGr(unittest.TestCase):
    def setUp(self):
        self.factory = Faker('el_GR')

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r'^EL\d{9}$', self.factory.vat_id())

    def test_police_id(self):
        for _ in range(100):
            assert re.search(r'^[ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ]{1,2} ?\d{6}$', self.factory.police_id())


class TestEnCA(unittest.TestCase):
    def setUp(self):
        self.factory = Faker('en_CA')
        self.factory.seed(0)

    def test_ssn(self):
        for _ in range(100):
            sin = self.factory.ssn()

            # Ensure that generated SINs are 11 characters long
            # including spaces, consist of spaces and digits only, and
            # satisfy the validation algorithm.
            assert len(sin) == 11
            assert sin.replace(' ', '').isdigit()
            assert ca_checksum(sin) == int(sin[-1])


class TestEnUS(unittest.TestCase):
    def setUp(self):
        self.factory = Faker('en_US')
        self.factory.seed(0)

    def test_ssn(self):
        for _ in range(100):
            ssn = self.factory.ssn(taxpayer_identification_number_type='SSN')

            # Ensure that generated SINs are 11 characters long
            # including dashes, consist of dashes and digits only, and
            # satisfy these requirements:
            #
            # An United States Social Security Number
            # (SSN) is a tax processing number issued by the Internal
            # Revenue Service with the format "AAA-GG-SSSS".  The
            # number is divided into three parts: the first three
            # digits, known as the area number because they were
            # formerly assigned by geographical region; the middle two
            # digits, known as the group number; and the final four
            # digits, known as the serial number. SSNs with the
            # following characteristics are not allocated:
            #
            # 1) Numbers with all zeros in any digit group
            # (000-##-####, ###-00-####, ###-##-0000).
            #
            # 2) Numbers with 666 or 900-999 in the first digit group.
            #
            # https://en.wikipedia.org/wiki/Social_Security_number

            assert len(ssn) == 11
            assert ssn.replace('-', '').isdigit()

            [area, group, serial] = ssn.split('-')

            assert 1 <= int(area) <= 899 and int(area) != 666
            assert 1 <= int(group) <= 99
            assert 1 <= int(serial) <= 9999
            assert area != '666'

    def test_invalid_ssn(self):
        self.factory.random = random2.Random()
        # Magic Numbers below generate '666-92-7944', '000-54-2963', '956-GG-9478', '436-00-1386',
        # and 134-76-0000 respectively. The "group" (GG) returned for '956-GG-9478 will be a random
        # number, and that random number is not in the "itin_group_numbers" List. The random GG occurs
        # even when using the same seed_instance() due to using random.choice() for GG to avoid valid
        # ITINs being returned as an invalid SSN:
        #
        # Ensure that generated SSNs are 11 characters long
        # including dashes, consist of dashes and digits only, and the tested number
        # violates the requirements below, ensuring an INVALID SSN is returned:
        #
        # A United States Social Security Number
        # (SSN) is a tax processing number issued by the Internal
        # Revenue Service with the format "AAA-GG-SSSS".  The
        # number is divided into three parts: the first three
        # digits, known as the area number because they were
        # formerly assigned by geographical region; the middle two
        # digits, known as the group number; and the final four
        # digits, known as the serial number. SSNs with the
        # following characteristics are not allocated:
        #
        # 1) Numbers with all zeros in any digit group
        # (000-##-####, ###-00-####, ###-##-0000).
        #
        # 2) Numbers with 666 or 900-999 in the first digit group.
        #
        # https://en.wikipedia.org/wiki/Social_Security_number
        #
        # ITIN explained:
        # https://www.irs.gov/individuals/international-taxpayers/general-itin-information

        itin_group_numbers = [
            70,
            71,
            72,
            73,
            74,
            75,
            76,
            77,
            78,
            79,
            80,
            81,
            82,
            83,
            84,
            85,
            86,
            87,
            88,
            90,
            91,
            92,
            94,
            95,
            96,
            97,
            98,
            99]

        self.factory.seed_instance(1143)
        ssn = self.factory.ssn(taxpayer_identification_number_type='INVALID_SSN')

        assert len(ssn) == 11
        assert ssn.replace('-', '').isdigit()
        assert ssn.startswith('666')

        self.factory.seed_instance(1514)
        ssn = self.factory.ssn(taxpayer_identification_number_type='INVALID_SSN')

        assert ssn.startswith('000')

        self.factory.seed_instance(2)
        ssn = self.factory.ssn(taxpayer_identification_number_type='INVALID_SSN')
        [area, group, serial] = ssn.split('-')

        assert 900 <= int(area) <= 999 and int(group) not in itin_group_numbers

        self.factory.seed_instance(9)
        ssn = self.factory.ssn(taxpayer_identification_number_type='INVALID_SSN')
        [area, group, serial] = ssn.split('-')

        assert int(area) < 900 and int(group) == 0

        self.factory.seed_instance(1)
        ssn = self.factory.ssn(taxpayer_identification_number_type='INVALID_SSN')
        [area, group, serial] = ssn.split('-')

        assert int(area) < 900 and int(serial) == 0

    def test_prohibited_ssn_value(self):
        # 666 is a prohibited value. The magic number selected as a seed
        # is one that would (if not specifically checked for) return an
        # SSN with an area of '666'.

        self.factory.seed(19031)
        ssn = self.factory.ssn()
        [area, group, serial] = ssn.split('-')
        assert area != '666'

    def test_itin(self):
        for _ in range(100):
            itin = self.factory.ssn(taxpayer_identification_number_type='ITIN')

            # Ensure that generated SINs are 11 characters long
            # including dashes, consist of dashes and digits only, and
            # satisfy these requirements:
            #
            # An United States Individual Taxpayer Identification Number
            # (ITIN) is a tax processing number issued by the Internal
            # Revenue Service. It is a nine-digit number that always begins
            # with the number 9 and has a range of 70-88 in the fourth and
            # fifth digit. Effective April 12, 2011, the range was extended
            # to include 900-70-0000 through 999-88-9999, 900-90-0000
            # through 999-92-9999 and 900-94-0000 through 999-99-9999.
            # https://www.irs.gov/individuals/international-taxpayers/general-itin-information

            assert len(itin) == 11
            assert itin.replace('-', '').isdigit()

            [area, group, serial] = itin.split('-')

            assert 900 <= int(area) <= 999
            assert 70 <= int(group) <= 88 or 90 <= int(group) <= 92 or 94 <= int(group) <= 99
            assert 0 <= int(serial) <= 9999

    def test_ein(self):
        ein_prefix_choices = [
            '01',
            '02',
            '03',
            '04',
            '05',
            '06',
            '10',
            '11',
            '12',
            '13',
            '14',
            '15',
            '16',
            '20',
            '21',
            '22',
            '23',
            '24',
            '25',
            '26',
            '27',
            '30',
            '31',
            '32',
            '33',
            '34',
            '35',
            '36',
            '37',
            '38',
            '39',
            '40',
            '41',
            '42',
            '43',
            '44',
            '45',
            '46',
            '47',
            '48',
            '50',
            '51',
            '52',
            '53',
            '54',
            '55',
            '56',
            '57',
            '58',
            '59',
            '60',
            '61',
            '62',
            '63',
            '64',
            '65',
            '66',
            '67',
            '68',
            '71',
            '72',
            '73',
            '74',
            '75',
            '76',
            '77',
            '80',
            '81',
            '82',
            '83',
            '84',
            '85',
            '86',
            '87',
            '88',
            '90',
            '91',
            '92',
            '93',
            '94',
            '95',
            '98',
            '99']

        for _ in range(100):
            ein = self.factory.ssn(taxpayer_identification_number_type='EIN')

            # An United States An Employer Identification Number (EIN) is
            # also known as a Federal Tax Identification Number, and is
            # used to identify a business entity. EINs follow a format of a
            # two-digit prefix followed by a hyphen and a seven-digit sequence.
            # https://www.irs.gov/businesses/small-businesses-self-employed/employer-id-numbers
            #
            # Ensure that generated EINs are 10 characters long
            # including a dash, consist of dashes and digits only, and
            # satisfy these requirements:
            #
            # There are only certain EIN Prefix values assigned:
            # https://www.irs.gov/businesses/small-businesses-self-employed/how-eins-are-assigned-and-valid-ein-prefixes

            assert len(ein) == 10
            assert ein.replace('-', '').isdigit()

            [prefix, sequence] = ein.split('-')

            assert prefix in ein_prefix_choices
            assert 0 <= int(sequence) <= 9999999

    def test_bad_tin_type(self):
        with self.assertRaises(ValueError):
            self.factory.ssn(taxpayer_identification_number_type='badValue')

    def test_wrong_tin_type_case(self):
        with self.assertRaises(ValueError):
            self.factory.ssn(taxpayer_identification_number_type='ssn')


class TestEsES(unittest.TestCase):
    def setUp(self):
        self.factory = Faker('es_ES')

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r'^ES\w\d{8}$|^ES\d{8}\w$|^ES\w\d{7}\w$', self.factory.vat_id())

    def test_nie(self):
        for _ in range(100):
            assert is_nie(self.factory.nie())

    def test_nif(self):
        for _ in range(100):
            assert is_nif(self.factory.nif())

    def test_cif(self):
        for _ in range(100):
            assert is_cif(self.factory.cif())

    def test_doi(self):
        assert len(self.factory.doi()) == 9


class TestEsCA(TestEsES):
    def setUp(self):
        self.factory = Faker('es_CA')


class TestEsMX(unittest.TestCase):
    def setUp(self):
        self.factory = Faker('es_MX')

    def test_ssn(self):
        for _ in range(100):
            ssn = self.factory.ssn()

            assert len(ssn) == 11
            assert ssn.isnumeric()
            assert mx_ssn_checksum(map(int, ssn[:-1])) == int(ssn[-1])

    def test_curp(self):
        for _ in range(100):
            curp = self.factory.curp()

            assert len(curp) == 18
            assert re.search(r'^[A-Z]{4}\d{6}[A-Z]{6}[0A]\d$', curp)
            assert mx_curp_checksum(curp[:-1]) == int(curp[-1])

    def test_rfc_natural(self):
        for _ in range(100):
            rfc = self.factory.rfc()

            assert len(rfc) == 13
            assert re.search(r'^[A-Z]{4}\d{6}[0-9A-Z]{3}$', rfc)

    def test_rfc_legal(self):
        for _ in range(100):
            rfc = self.factory.rfc(natural=False)

            assert len(rfc) == 12
            assert re.search(r'^[A-Z]{3}\d{6}[0-9A-Z]{3}$', rfc)


class TestEtEE(unittest.TestCase):
    """ Tests SSN in the et_EE locale """

    def setUp(self):
        self.factory = Faker('et_EE')

    def test_ssn_checksum(self):
        assert et_checksum([4, 4, 1, 1, 1, 3, 0, 4, 9, 2]) == 3
        assert et_checksum([3, 6, 7, 0, 1, 1, 6, 6, 2, 7]) == 8
        assert et_checksum([4, 7, 0, 0, 4, 2, 1, 5, 0, 1]) == 2
        assert et_checksum([3, 9, 7, 0, 3, 0, 4, 3, 3, 6]) == 0

    @freezegun.freeze_time('2019-03-11')
    def test_ssn(self):
        self.factory.random = random2.Random()

        self.factory.seed_instance(0)
        value = self.factory.ssn()
        assert re.search(r'^\d{11}$', value)
        assert not value.endswith('0')

        self.factory.seed_instance(5)
        value = self.factory.ssn()

        assert re.search(r'^\d{11}$', value)
        assert value.endswith('0')

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r'^EE\d{9}$', self.factory.vat_id())


class TestFiFI(unittest.TestCase):
    """ Tests SSN in the fi_FI locale """

    def setUp(self):
        self.factory = Faker('fi_FI')
        self.provider = fi_Provider

    def test_century_code(self):
        assert self.provider._get_century_code(1900) == '-'
        assert self.provider._get_century_code(1999) == '-'
        assert self.provider._get_century_code(2000) == 'A'
        assert self.provider._get_century_code(2999) == 'A'
        assert self.provider._get_century_code(1800) == '+'
        assert self.provider._get_century_code(1899) == '+'
        with pytest.raises(ValueError):
            self.provider._get_century_code(1799)
        with pytest.raises(ValueError):
            self.provider._get_century_code(3000)

    def test_ssn_sanity(self):
        for age in range(100):
            self.factory.ssn(min_age=age, max_age=age + 1)

    def test_valid_ssn(self):
        ssn = self.factory.ssn(artificial=False)
        individual_number = int(ssn[7:10])
        assert individual_number <= 899

    def test_artifical_ssn(self):
        ssn = self.factory.ssn(artificial=True)
        individual_number = int(ssn[7:10])
        assert individual_number >= 900

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r'^FI\d{8}$', self.factory.vat_id())


class TestFrFR(unittest.TestCase):
    def setUp(self):
        self.factory = Faker('fr_FR')

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r'^FR[\w\d]{2} \d{9}$', self.factory.vat_id())


class TestEnGB(unittest.TestCase):
    def setUp(self):
        self.factory = Faker('en_GB')

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r'^GB\d{3} \d{4} \d{2}(?: \d{3})?$|^GB(?:GD|HA)\d{3}$', self.factory.vat_id())


class TestHrHR(unittest.TestCase):
    """ Tests SSN in the hr_HR locale """

    def setUp(self):
        self.factory = Faker('hr_HR')

    def test_ssn_checksum(self):
        assert hr_checksum([0, 0, 2, 2, 8, 2, 6, 9, 2, 8]) == 9
        assert hr_checksum([5, 8, 9, 3, 6, 9, 5, 1, 2, 5]) == 1
        assert hr_checksum([5, 7, 8, 0, 2, 0, 3, 4, 2, 3]) == 7
        assert hr_checksum([4, 3, 3, 3, 1, 4, 6, 7, 6, 2]) == 2
        assert hr_checksum([0, 5, 9, 3, 7, 7, 5, 9, 1, 8]) == 7
        assert hr_checksum([7, 1, 1, 4, 9, 9, 1, 2, 4, 1]) == 6

    def test_ssn(self):
        for _ in range(100):
            assert re.search(r'^\d{11}$', self.factory.ssn())

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r'^HR\d{11}$', self.factory.vat_id())


class TestHuHU(unittest.TestCase):
    def setUp(self):
        self.factory = Faker('hu_HU')
        self.factory.seed(0)

    def test_ssn(self):
        for _ in range(100):
            ssn = self.factory.ssn()
            assert ssn.isdigit()
            assert len(ssn) >= 10
            assert len(ssn) <= 12

        for _ in range(100):
            dob_val = '{:02d}{:02d}{:02d}'.format(
                self.factory.random_int(0, 99),
                self.factory.random_int(1, 12),
                self.factory.random_int(1, 31))
            dob = self.factory.random.choice([None, dob_val])
            gender = self.factory.random.choice([None, 'F', 'M', 'z'])
            try:
                ssn = self.factory.ssn(dob=dob, gender=gender)
                assert ssn.isdigit()
                assert len(ssn) >= 10
                assert len(ssn) <= 12
            except ValueError:
                pass

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r'^HU\d{8}$', self.factory.vat_id())


class TestPtBR(unittest.TestCase):
    def setUp(self):
        self.factory = Faker('pt_BR')

    def test_pt_BR_ssn_checksum(self):
        assert pt_checksum([8, 8, 2, 8, 2, 1, 6, 5, 2]) == 2
        assert pt_checksum([8, 8, 2, 8, 2, 1, 6, 5, 2, 2]) == 0

    def test_pt_BR_ssn(self):
        for _ in range(100):
            assert re.search(r'^\d{11}$', self.factory.ssn())

    def test_pt_BR_cpf(self):
        for _ in range(100):
            assert re.search(r'\d{3}\.\d{3}\.\d{3}-\d{2}', self.factory.cpf())

    def test_pt_BR_rg(self):
        for _ in range(100):
            to_test = self.factory.rg()
            if 'X' in to_test:
                assert re.search(r'^\d{8}X', to_test)
            else:
                assert re.search(r'^\d{9}$', to_test)


class TestNlNL(unittest.TestCase):
    def setUp(self):
        self.factory = Faker('nl_NL')

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r'^NL\d{9}B\d{2}$', self.factory.vat_id())


class TestNoNO(unittest.TestCase):
    def setUp(self):
        self.factory = Faker('no_NO')

    def test_no_NO_ssn_checksum(self):
        assert no_checksum([0, 1, 0, 2, 0, 3, 9, 8, 7], no_Provider.scale1) == 6
        assert no_checksum([0, 1, 0, 2, 0, 3, 9, 8, 7, 6], no_Provider.scale2) == 7

    def test_no_NO_ssn(self):
        for _ in range(100):
            ssn = self.factory.ssn()
            assert ssn.isdigit()
            assert len(ssn) == 11

    def test_no_NO_ssn_dob_passed(self):
        test_data = [('20010203', '030201'),
                     ('19991231', '311299')]
        for date_of_birth, expected_dob_part in test_data:
            ssn = self.factory.ssn(dob=date_of_birth)
            assert ssn[:6] == expected_dob_part

    def test_no_NO_ssn_invalid_dob_passed(self):
        with pytest.raises(ValueError):
            self.factory.ssn(dob='010401')
        with pytest.raises(ValueError):
            self.factory.ssn(dob='hello_world')
        with pytest.raises(ValueError):
            self.factory.ssn(dob='001301')

    def test_no_NO_ssn_gender_passed(self):
        # Females have even number at index 8
        ssn = self.factory.ssn(gender='F')
        assert int(ssn[8]) % 2 == 0
        # Males have odd number at index 8
        ssn = self.factory.ssn(gender='M')
        assert int(ssn[8]) % 2 == 1

    def test_no_NO_ssn_invalid_gender_passed(self):
        with pytest.raises(ValueError):
            self.factory.ssn(gender='A')


class TestPlPL(unittest.TestCase):
    """ Tests SSN in the pl_PL locale """

    def setUp(self):
        self.factory = Faker('pl_PL')

    def test_ssn_checksum(self):
        assert pl_checksum([0, 5, 2, 6, 2, 8, 1, 2, 3, 6]) == 5
        assert pl_checksum([8, 5, 0, 5, 0, 8, 1, 5, 5, 8]) == 7
        assert pl_checksum([4, 5, 1, 1, 1, 0, 0, 2, 4, 3]) == 3
        assert pl_checksum([9, 1, 0, 7, 2, 6, 1, 4, 8, 7]) == 3
        assert pl_checksum([8, 1, 1, 2, 1, 4, 1, 1, 8, 7]) == 6

    def test_calculate_month(self):
        assert pl_calculate_mouth(datetime.strptime('1 1 1900', '%m %d %Y')) == 1
        assert pl_calculate_mouth(datetime.strptime('12 1 1900', '%m %d %Y')) == 12
        assert pl_calculate_mouth(datetime.strptime('1 1 1999', '%m %d %Y')) == 1

        assert pl_calculate_mouth(datetime.strptime('1 1 2000', '%m %d %Y')) == 21
        assert pl_calculate_mouth(datetime.strptime('12 1 2000', '%m %d %Y')) == 32
        assert pl_calculate_mouth(datetime.strptime('1 1 2099', '%m %d %Y')) == 21

        assert pl_calculate_mouth(datetime.strptime('1 1 2100', '%m %d %Y')) == 41
        assert pl_calculate_mouth(datetime.strptime('12 1 2100', '%m %d %Y')) == 52
        assert pl_calculate_mouth(datetime.strptime('1 1 2199', '%m %d %Y')) == 41

        assert pl_calculate_mouth(datetime.strptime('1 1 2200', '%m %d %Y')) == 61
        assert pl_calculate_mouth(datetime.strptime('12 1 2200', '%m %d %Y')) == 72
        assert pl_calculate_mouth(datetime.strptime('1 1 2299', '%m %d %Y')) == 61

    def test_ssn(self):
        for _ in range(100):
            assert re.search(r'^\d{11}$', self.factory.ssn())

    def test_vat_id(self):
        for _ in range(100):
            assert re.search(r'^PL\d{10}$', self.factory.vat_id())


class TestEnPh(unittest.TestCase):
    num_sample_runs = 1000

    def setUp(self):
        self.sss_pattern = re.compile(r'^\d{2}-\d{7}-\d$')
        self.gsis_pattern = re.compile(r'^\d{11}$')
        self.philhealth_pattern = re.compile(r'^\d{2}-\d{9}-\d$')
        self.pagibig_pattern = re.compile(r'^\d{4}-\d{4}-\d{4}$')
        self.umid_pattern = re.compile(r'^\d{4}-\d{7}-\d$')
        self.setup_factory()

    def setup_factory(self):
        self.factory = Faker('en_PH')

    def test_PH_sss(self):
        for i in range(self.num_sample_runs):
            assert self.sss_pattern.match(self.factory.sss())

    def test_PH_gsis(self):
        for i in range(self.num_sample_runs):
            assert self.gsis_pattern.match(self.factory.gsis())

    def test_PH_philhealth(self):
        for i in range(self.num_sample_runs):
            assert self.philhealth_pattern.match(self.factory.philhealth())

    def test_PH_pagibig(self):
        for i in range(self.num_sample_runs):
            assert self.pagibig_pattern.match(self.factory.pagibig())

    def test_PH_umid(self):
        for i in range(self.num_sample_runs):
            assert self.umid_pattern.match(self.factory.umid())


class TestFilPh(TestEnPh):

    def setup_factory(self):
        self.factory = Faker('fil_PH')


class TestTlPh(TestEnPh):

    def setup_factory(self):
        self.factory = Faker('tl_PH')
