tld_dict = {'.ac': 'Ascension Island', '.ad': 'Andorra', '.ae': 'United Arab Emirates', '.af': 'Afghanistan',
            '.ag': 'Antigua and Barbuda', '.ai': 'Anguilla', '.al': 'Albania', '.am': 'Armenia',
            '.an': 'Netherlands Antilles', '.ao': 'Angola', '.aq': 'Antarctic', '.ar': 'Argentina',
            '.as': 'American Samoa', '.at': 'Austria', '.au': 'Australia', '.aw': 'Aruba', '.ax': 'Åland Islands',
            '.az': 'Azerbaijan', '.ba': 'Bosnia and Herzegovina', '.bb': 'Barbados', '.bd': 'Bangladesh',
            '.be': 'Belgium', '.bf': 'Burkina\xa0Faso', '.bg': 'Bulgaria', '.bh': 'Bahrain', '.bi': 'Burundi',
            '.bj': 'Benin', '.bl': 'Saint-Barthélemy', '.bm': 'Bermuda', '.bn': 'Brunei', '.bo': 'Bolivia',
            '.br': 'Brazil', '.bq': 'Bonaire', '.bs': 'Bahamas', '.bt': 'Bhutan', '.bv': 'Bouvet Island',
            '.bw': 'Botswana', '.by': 'Belarus', '.bz': 'Belize', '.ca': 'Canada', '.cc': 'Cocos Islands',
            '.cd': 'Democratic Republic of the Congo', '.cf': 'Central African Republic',
            '.cg': 'Republic of the Congo', '.ch': 'Switzerland', '.ci': 'Côte d’Ivoire', '.ck': 'Cook Islands',
            '.cl': 'Chile', '.cm': 'Cameroon', '.cn': 'China', '.co': 'Colombia', '.cr': 'Costa\xa0Rica',
            '.cs': 'Czechoslovakia', '.cu': 'Cuba', '.cv': 'Cape\xa0Verde', '.cw': 'Curaçao', '.cx': 'Christmas Island',
            '.cy': 'Cyprus', '.cz': 'Czech Republic', '.dd': 'German Democratic Republic', '.de': 'Germany',
            '.dj': 'Djibuti', '.dk': 'Denmark', '.dm': 'Dominica', '.do': 'Dominican Republic', '.dz': 'Algeria',
            '.ec': 'Ecuador', '.ee': 'Estonia', '.eg': 'Egypt', '.eh': 'Western Sahara', '.er': 'Eritrea',
            '.es': 'Spain', '.et': 'Ethiopia', '.eu': 'European Union', '.fi': 'Finland', '.fj': 'Fiji',
            '.fk': 'Falkland Islands', '.fm': 'Micronesia', '.fo': 'Faroe', '.fr': 'France', '.ga': 'Gabon',
            '.gb': 'United Kingdom', '.gd': 'Grenada', '.ge': 'Georgia', '.gf': 'French Guiana', '.gg': 'Guernsey',
            '.gh': 'Ghana', '.gi': 'Gibraltar', '.gl': 'Greenland', '.gm': 'Gambia', '.gn': 'Guinea',
            '.gp': 'Guadeloupe', '.gq': 'Equatorial Guinea', '.gr': 'Greece',
            '.gs': 'South Georgia and the South Sandwich Islands', '.gt': 'Guatemala', '.gu': 'Guam',
            '.gw': 'Guinea-Bissau', '.gy': 'Guyana', '.hk': 'Hong Kong', '.hm': 'Heard Island and McDonald Islands',
            '.hn': 'Honduras', '.hr': 'Croatia', '.ht': 'Haiti', '.hu': 'Hungary', '.id': 'Indonesia', '.ie': 'Ireland',
            '.il': 'Israel', '.im': 'Isle\xa0of\xa0Man', '.in': 'India', '.io': 'British Indian Ocean Territory',
            '.iq': 'Iraq', '.ir': 'Iran', '.is': 'Iceland', '.it': 'Italy', '.je': 'Jersey', '.jm': 'Jamaica',
            '.jo': 'Jordan', '.jp': 'Japan', '.ke': 'Kenya', '.kg': 'Kyrgyzstan', '.kh': 'Cambodia', '.ki': 'Kiribati',
            '.km': 'Comoros', '.kn': 'St. Kitts and Nevis', '.kp': 'North Korea', '.kr': 'South Korea', '.kw': 'Kuwait',
            '.ky': 'Cayman Islands', '.kz': 'Kazakhstan', '.la': 'Laos', '.lb': 'Lebanon', '.lc': 'St.\xa0Lucia',
            '.li': 'Liechtenstein', '.lk': 'Sri\xa0Lanka', '.lr': 'Liberia', '.ls': 'Lesotho', '.lt': 'Lithuania',
            '.lu': 'Luxembourg', '.lv': 'Latvia', '.ly': 'Libya', '.ma': 'Marocco', '.mc': 'Monaco', '.md': 'Moldova',
            '.me': 'Montenegro', '.mf': 'Saint Martin', '.mg': 'Madagascar', '.mh': 'Marshall Islands',
            '.mk': 'Macedonia', '.ml': 'Mali', '.mm': 'Myanmar', '.mn': 'Mongolia', '.mo': 'Macau',
            '.mp': 'Northern Mariana Islands', '.mq': 'Martinique', '.mr': 'Mauritania', '.ms': 'Montserrat',
            '.mt': 'Malta', '.mu': 'Mauritius', '.mv': 'Maldives', '.mw': 'Malawi', '.mx': 'Mexico', '.my': 'Malaysia',
            '.mz': 'Mozambique', '.na': 'Namibia', '.nc': 'New Caledonia', '.ne': 'Niger', '.nf': 'Norfolk Island',
            '.ng': 'Nigeria', '.ni': 'Nicaragua', '.nl': 'Netherlands', '.no': 'Norway', '.np': 'Nepal', '.nr': 'Nauru',
            '.nu': 'Niue', '.nz': 'New Zealand', '.om': 'Oman', '.pa': 'Panama', '.pe': 'Peru',
            '.pf': 'French Polynesia', '.pg': 'Papua New Guinea', '.ph': 'Philippines', '.pk': 'Pakistan',
            '.pl': 'Poland', '.pm': 'Saint Pierre and Miquelon', '.pn': 'Pitcairn Islands', '.pr': 'Puerto\xa0Rico',
            '.ps': 'Palestine', '.pt': 'Portugal', '.pw': 'Palau', '.py': 'Paraguay', '.qa': 'Qatar', '.re': 'Réunion',
            '.ro': 'Romania', '.rs': 'Serbia', '.ru': 'Russia', '.rw': 'Rwanda', '.sa': 'Saudi Arabia',
            '.sb': 'Solomon Islands', '.sc': 'Seychelles', '.sd': 'Sudan', '.se': 'Sweden', '.sg': 'Singapore',
            '.sh': 'St. Helena', '.si': 'Slovenia', '.sj': 'Svalbard and Jan Mayen', '.sk': 'Slovakia',
            '.sl': 'Sierra\xa0Leone', '.sm': 'San\xa0Marino', '.sn': 'Senegal', '.so': 'Somalia', '.sr': 'Suriname',
            '.ss': 'South Sudan', '.st': 'São\xa0Tomé and Príncipe', '.su': 'Soviet Union', '.sv': 'El\xa0Salvador',
            '.sx': 'Sint Maarten', '.sy': 'Syria', '.sz': 'Swaziland', '.tc': 'Turks and Caicos Islands', '.td': 'Chad',
            '.tf': 'French Southern and Antarctic Lands', '.tg': 'Togo', '.th': 'Thailand', '.tj': 'Tajikistan',
            '.tk': 'Tokelau', '.tl': 'Timor-Leste', '.tm': 'Turkmenistan', '.tn': 'Tunisia', '.to': 'Tonga',
            '.tp': 'Timor-Leste', '.tr': 'Turkey', '.tt': 'Trinidad and Tobago', '.tv': 'Tuvalu', '.tw': 'Taiwan',
            '.tz': 'Tanzania', '.ua': 'Ukraine', '.ug': 'Uganda', '.uk': 'United Kingdom',
            '.um': 'United States Minor Outlying Islands', '.us': 'United States', '.uy': 'Uruguay',
            '.uz': 'Uzbekistan', '.va': 'Vatican City', '.vc': 'St.\xa0Vincent and the Grenadines', '.ve': 'Venezuela',
            '.vg': 'Britische Virgin Islands', '.vi': 'United States Virgin Islands', '.vn': 'Vietnam',
            '.vu': 'Vanuatu', '.wf': 'Wallis and Futuna', '.ws': 'Samoa', '.ye': 'Yemen', '.yt': 'Mayotte',
            '.yu': 'Yugoslavia', '.za': 'South Africa', '.zm': 'Zambia', '.zr': 'Zaire', '.zw': 'Zimbabwe'}


def tld_analyser(URL: str) -> str:
    # TODO implement
    # assume that the protocoll is always included (https:// for example) but there doesn't have to be a path after the domain
    URL = str.rsplit(URL, "/")
    main_url = URL[2]
    domain = main_url[-3:]
    result = tld_dict[domain]
    return result
    pass


def main() -> None:
    # Tests for student side debugging only
    result = tld_analyser(
        "https://gibtesheuteschnitzel.de"
    )
    expected = "Germany"
    assert result == expected
    result = tld_analyser(
        "https://italiandesignoutlet.it/en/lighting/1731-lamp-ghalia-so-compo-12l-light4.html"
    )
    expected = "Italy"
    assert result == expected
    result = tld_analyser(
        "https://www.noelleeming.co.nz/p/goldair-fleecy-topper-fitted-electric-blanket---king-single/N189958.html"
    )
    expected = "New Zealand"
    assert result == expected


if __name__ == '__main__':
    main()
