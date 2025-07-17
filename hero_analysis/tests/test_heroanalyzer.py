from hero_analysis.heroanalyzer import HeroAnalyzer
import pytest
   
@pytest.mark.parametrize("values1, values2, expected_result", [
    ('Female', False, '193'),   #test by valid datas
    ('Male', True, '876'),      #test by valid datas
    ('Female', True, '366'),    #test by valid datas    
    ('Male', False, '975'),     #test by valid datas
    ('female', True, '366'),    #test by register
    ('FEMALE', False, '193'),   #test by register
    ('MALE', True, '876'),      #test by register
    ('male', False, '975'),     #test by register
    ('Male', "True", 'Not bool type!'),     #test data type by work
    ('Male', "False", 'Not bool type!'),    #test data type by work
    ('Female', "True", 'Not bool type!'),   #test data type by work
    ('Female', "False", 'Not bool type!'),  #test data type by work
    ('asd', False, 'No datas!'),            #test invalid datas
    ('FemaleMale', True, 'No datas!'),      #test invalid datas
    ('MaleFemale', False, 'No datas!'),     #test invalid datas
    ('123', False, 'No datas!'),            #test invalid datas
    ])

def test_class(values1,values2,expected_result):
    test = HeroAnalyzer(values1,values2)
    assert test.main() == expected_result