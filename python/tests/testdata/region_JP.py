"""Auto-generated file, do not edit by hand. JP metadata"""
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_JP = PhoneMetadata(id='JP', country_code=81, international_prefix='010',
    general_desc=PhoneNumberDesc(national_number_pattern='07\\d{5}|[1-357-9]\\d{3,10}', possible_number_pattern='\\d{4,11}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='07\\d{5}|[1-357-9]\\d{3,10}', possible_number_pattern='\\d{4,11}'),
    mobile=PhoneNumberDesc(national_number_pattern='07\\d{5}|[1-357-9]\\d{3,10}', possible_number_pattern='\\d{4,11}'),
    toll_free=PhoneNumberDesc(national_number_pattern='0777[01]\\d{2}', possible_number_pattern='\\d{7}', example_number='0777012'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    short_code=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    standard_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='[23]\\d{3}', possible_number_pattern='\\d{4}'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{4})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[57-9]0'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3 \\4', leading_digits_pattern=['[57-9]0'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['111|222|333', '(?:111|222|333)1', '(?:111|222|333)11'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{4})(\\d)(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['222|333', '2221|3332', '22212|3332', '222120|3332'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{2})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['[23]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{4})', format=u'\\1-\\2', leading_digits_pattern=['077'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{4})', format=u'*\\1', leading_digits_pattern=['[23]'], national_prefix_formatting_rule=u'\\1')],
    leading_zero_possible=True)
