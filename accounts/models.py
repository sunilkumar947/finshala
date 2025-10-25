from django.db import models
from django.contrib.auth.models import AbstractUser

TAX_STATUS_CHOICES = [
        ('01', 'Individual'),
        ('02', 'On behalf of minor'),
        ('03', 'HUF'),
        ('04', 'Company'),
        ('05', 'AOP'),
        ('06', 'Partnership Firm'),
        ('07', 'Body Corporate'),
        ('08', 'Trust'),
        ('09', 'Society'),
        ('10', 'Others'),
        ('11', 'NRI-Others'),
        ('12', 'DFI'),
        ('13', 'Sole Proprietorship'),
        ('21', 'NRE'),
        ('22', 'OCB'),
        ('23', 'FII'),
        ('24', 'NRO'),
        ('25', 'Overseas Corp. Body - Others'),
        ('26', 'NRI Child'),
        ('27', 'NRI - HUF (NRO)'),
        ('28', 'NRI - Minor (NRO)'),
        ('29', 'NRI - HUF (NRE)'),
        ('31', 'Provident Fund'),
        ('32', 'Super Annuation Fund'),
        ('33', 'Gratuity Fund'),
        ('34', 'Pension Fund'),
        ('36', 'Mutual Funds FOF Schemes'),
        ('37', 'NPS Trust'),
        ('38', 'Global Development Network'),
        ('39', 'FCRA'),
        ('41', 'QFI - Individual'),
        ('42', 'QFI - Minors'),
        ('43', 'QFI - Corporate'),
        ('44', 'QFI - Pension Funds'),
        ('45', 'QFI - Hedge Funds'),
        ('46', 'QFI - Mutual Funds'),
        ('47', 'LLP'),
        ('48', 'Non-Profit organization [NPO]'),
        ('51', 'Public Limited Company'),
        ('52', 'Private Limited Company'),
        ('53', 'Unlisted Company'),
        ('54', 'Mutual Funds'),
        ('55', 'FPI - Category I'),
        ('56', 'FPI - Category II'),
        ('57', 'FPI - Category III'),
        ('58', 'Financial Institutions'),
        ('59', 'Body of Individuals, Insurance Company'),
        ('60', 'OCI - Repatriation'),
        ('61', 'OCI - Non-Repatriation'),
        ('62', 'Person of Indian Origin'),
        ('70', 'Government Body'),
        ('72', 'Defense Establishment'),
        ('73', 'Non - Government Organisation'),
        ('74', 'Bank/Co-Operative Bank'),
        ('75', 'Artificial Juridical Person'),
        ('76', 'Seafarer NRE'),
        ('77', 'Seafarer NRO'),
        ('78', 'Local Authority'),
        ('79', 'Other'),
    ]

OCCUPATION_CHOICES = [
        ('01', 'Business'),
        ('02', 'Services'),
        ('03', 'Professional'),
        ('04', 'Agriculture'),
        ('05', 'Retired'),
        ('06', 'Housewife'),
        ('07', 'Student'),
        ('08', 'Others'),
    ]

ACCOUNT_TYPE = [
        ('SB', 'Savings Bank'),
        ('CB', 'Current Bank'),
        ('NE', 'NRE Account'),
        ('NO', 'NRO Account'),
    ]
    
class User(AbstractUser):
    ROLE_CHOICE =[
        ('S','superadmin'),
        ('A','agent'),
        ('U','user')
    ]

    role = models.CharField(max_length=2, choices=ROLE_CHOICE, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(unique=True, max_length=15, null=True, blank=True)
    otp             = models.CharField(max_length=10,null=True)
    created_time 	= models.DateTimeField(auto_now_add=True, null=True, blank=True)
    utimestamp 		= models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{str(self.phone)}, {self.email}"	
    
    REQUIRED_FIELDS = ['phone']
    
class Agent(models.Model):
    ARN_CHOICE = [
        ('Y', 'Yes'), 
        ('N', 'No'),
    ]

    ADDRESS_PROOF_CHOICE = [
        ('A', "Aadhaar Card"),
        ('B', "Voter ID"),
        ('C', "Driving License"),
        ('D', "Passport")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    agent_id = models.CharField(max_length=10, null=True, blank=True)
    account_type = models.CharField(max_length=2, choices=ACCOUNT_TYPE, null=True, blank=True)
    bank_name = models.CharField(max_length=255, null=True, blank=True)
    acco_no = models.CharField(max_length=20, null=True, blank=True)
    reenter_account_no = models.CharField(max_length=20, null=True, blank=True)
    ifsc_code = models.CharField(max_length=15, null=True, blank=True)
    account_holdername = models.CharField(max_length=255, null=True, blank=True)
    ARN = models.CharField(max_length=2, choices=ARN_CHOICE, null=True, blank=True)
    ARN_no = models.CharField(max_length=6, null=True, blank=True)
    ARN_card_image = models.ImageField(upload_to="ARN image/", null=True, blank=True)
    photo = models.ImageField(upload_to="yourphoto/", null=True, blank=True)
    pan_card_image = models.ImageField(upload_to="pancard/", null=True, blank=True)
    address_proof = models.CharField(max_length=2, choices=ADDRESS_PROOF_CHOICE, null=True, blank=True)
    front_image = models.ImageField(upload_to='frontimage/', null=True, blank=True)
    back_image = models.ImageField(upload_to="backimage/", null=True, blank=True)
    EUIN_card_image = models.ImageField(upload_to="EUIN card image/", null=True, blank=True)
    NISM_certificate_image = models.ImageField(upload_to="NISM certificate image/", null=True, blank=True)
    created_time 	= models.DateTimeField(auto_now_add=True, null=True, blank=True)
    utimestamp 		= models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.agent_id
    
class Uccregister(models.Model):
    REGN_TYPE = [
        ('NEW', 'NEW'),
        ('MOD', 'MOD'),	
    ]

    CLIENT_HOLDING_CHOICES = [
        ('SI', 'Single'),
        ('JO', 'Joint'),
        ('AS', 'Anyone or Survivor'),
    ]
    
    PAN_EXEMPT_CATEGORY_CHOICES = [
        ('01', 'SIKKIM Resident'),
        ('02', 'Transactions carried out on behalf of STATE GOVT'),
        ('03', 'Transactions carried out on behalf of CENTRAL GOVT'),
        ('04', 'COURT APPOINTED OFFICIALS'),
        ('05', 'UN Entity/Multilateral agency exempt from paying tax in India'),
        ('06', 'Official Liquidator'),
        ('07', 'Court Receiver'),
        ('08', 'Investment in Mutual Funds Upto Rs. 50,000/- p.a. including SIP'),
    ]
    
    Client_Type = [
        ('P', 'Physical'),
        ('D', 'Demat'),
    ]
    
    DIVIDEND_PAYMODE = [
        ('01', 'Cheque'),
        ('02', 'Direct Credit'),
        ('03', 'ECS'),
        ('04', 'NEFT'),
        ('05', 'RTGS'),
    ]
    
    STATE_CODE_CHOICES = [
        ('AN', 'Andaman & Nicobar'),
        ('AR', 'Arunachal Pradesh'),
        ('AP', 'Andhra Pradesh'),
        ('AS', 'Assam'),
        ('BH', 'Bihar'),
        ('CH', 'Chandigarh'),
        ('CG', 'Chhattisgarh'),
        ('GO', 'Goa'),
        ('GU', 'Gujarat'),
        ('HA', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JM', 'Jammu & Kashmir'),
        ('JK', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KE', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MA', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ME', 'Meghalaya'),
        ('MI', 'Mizoram'),
        ('NA', 'Nagaland'),
        ('ND', 'New Delhi'),
        ('OR', 'Orissa'),
        ('PO', 'Pondicherry'),
        ('PU', 'Punjab'),
        ('RA', 'Rajasthan'),
        ('SI', 'Sikkim'),
        ('TG', 'Telangana'),
        ('TN', 'Tamil Nadu'),
        ('TR', 'Tripura'),
        ('UP', 'Uttar Pradesh'),
        ('UC', 'Uttaranchal'),
        ('WB', 'West Bengal'),
        ('DN', 'Dadra and Nagar Haveli'),
        ('DD', 'Daman and Diu'),
        ('LD', 'Lakshadweep'),
        ('OH', 'Others'),
    ]
    
    COUNTRY_CODE_CHOICES = [
        ('001', 'Afghanistan'),
        ('002', 'Aland Islands'),
        ('003', 'Albania'),
        ('004', 'Algeria'),
        ('005', 'American Samoa'),
        ('006', 'Andorra'),
        ('007', 'Angola'),
        ('008', 'Anguilla'),
        ('009', 'Antarctica'),
        ('010', 'Antigua And Barbuda'),
        ('011', 'Argentina'),
        ('012', 'Armenia'),
        ('013', 'Aruba'),
        ('014', 'Australia'),
        ('015', 'Austria'),
        ('016', 'Azerbaijan'),
        ('017', 'Bahamas'),
        ('018', 'Bahrain'),
        ('019', 'Bangladesh'),
        ('020', 'Barbados'),
        ('021', 'Belarus'),
        ('022', 'Belgium'),
        ('023', 'Belize'),
        ('024', 'Benin'),
        ('025', 'Bermuda'),
        ('026', 'Bhutan'),
        ('027', 'Bolivia'),
        ('028', 'Bosnia And Herzegovina'),
        ('029', 'Botswana'),
        ('030', 'Bouvet Island'),
        ('031', 'Brazil'),
        ('032', 'British Indian Ocean Territory'),
        ('033', 'Brunei Darussalam'),
        ('034', 'Bulgaria'),
        ('035', 'Burkina Faso'),
        ('036', 'Burundi'),
        ('037', 'Cambodia'),
        ('038', 'Cameroon'),
        ('039', 'Canada'),
        ('040', 'Cape Verde'),
        ('041', 'Cayman Islands'),
        ('042', 'Central African Republic'),
        ('043', 'Chad'),
        ('044', 'Chile'),
        ('045', 'China'),
        ('046', 'Christmas Island'),
        ('047', 'Cocos (Keeling) Islands'),
        ('048', 'Colombia'),
        ('049', 'Comoros'),
        ('050', 'Congo'),
        ('051', 'Congo, The Democratic Republic Of The'),
        ('052', 'Cook Islands'),
        ('053', 'Costa Rica'),
        ('054', 'Cote DIvoire'),
        ('055', 'Croatia'),
        ('056', 'Cuba'),
        ('057', 'Cyprus'),
        ('058', 'Czech Republic'),
        ('059', 'Denmark'),
        ('060', 'Djibouti'),
        ('061', 'Dominica'),
        ('062', 'Dominican Republic'),
        ('063', 'Ecuador'),
        ('064', 'Egypt'),
        ('065', 'El Salvador'),
        ('066', 'Equatorial Guinea'),
        ('067', 'Eritrea'),
        ('068', 'Estonia'),
        ('069', 'Ethiopia'),
        ('070', 'Falkland Islands (Malvinas)'),
        ('071', 'Faroe Islands'),
        ('072', 'Fiji'),
        ('073', 'Finland'),
        ('074', 'France'),
        ('075', 'French Guiana'),
        ('076', 'French Polynesia'),
        ('077', 'French Southern Territories'),
        ('078', 'Gabon'),
        ('079', 'Gambia'),
        ('080', 'Georgia'),
        ('081', 'Germany'),
        ('082', 'Ghana'),
        ('083', 'Gibraltar'),
        ('084', 'Greece'),
        ('085', 'Greenland'),
        ('086', 'Grenada'),
        ('087', 'Guadeloupe'),
        ('088', 'Guam'),
        ('089', 'Guatemala'),
        ('090', 'Guernsey'),
        ('091', 'Guinea'),
        ('092', 'Guinea-Bissau'),
        ('093', 'Guyana'),
        ('094', 'Haiti'),
        ('095', 'Heard Island And Mcdonald Islands'),
        ('096', 'Holy See (Vatican City State)'),
        ('097', 'Honduras'),
        ('098', 'Hong Kong'),
        ('099', 'Hungary'),
        ('100', 'Iceland'),
        ('India', 'India'),
        ('102', 'Indonesia'),
        ('103', 'Iran, Islamic Republic Of'),
        ('104', 'Iraq'),
        ('105', 'Ireland'),
        ('106', 'Isle Of Man'),
        ('107', 'Israel'),
        ('108', 'Italy'),
        ('109', 'Jamaica'),
        ('110', 'Japan'),
        ('111', 'Jersey'),
        ('112', 'Jordan'),
        ('113', 'Kazakhstan'),
        ('114', 'Kenya'),
        ('115', 'Kiribati'),
        ('116', 'Korea, Democratic Peoples Republic Of'),
        ('117', 'Korea, Republic Of'),
        ('118', 'Kuwait'),
        ('119', 'Kyrgyzstan'),
        ('120', 'Lao Peoples Democratic Republic'),
        ('121', 'Latvia'),
        ('122', 'Lebanon'),
        ('123', 'Lesotho'),
        ('124', 'Liberia'),
        ('125', 'Libyan Arab Jamahiriya'),
        ('126', 'Liechtenstein'),
        ('127', 'Lithuania'),
        ('128', 'Luxembourg'),
        ('129', 'Macao'),
        ('130', 'Macedonia, The Former Yugoslav Republic Of'),
        ('131', 'Madagascar'),
        ('132', 'Malawi'),
        ('133', 'Malaysia'),
        ('134', 'Maldives'),
        ('135', 'Mali'),
        ('136', 'Malta'),
        ('137', 'Marshall Islands'),
        ('138', 'Martinique'),
        ('139', 'Mauritania'),
        ('140', 'Mauritius'),
        ('141', 'Mayotte'),
        ('142', 'Mexico'),
        ('143', 'Micronesia, Federated States Of'),
        ('144', 'Moldova, Republic Of'),
        ('145', 'Monaco'),
        ('146', 'Mongolia'),
        ('147', 'Montserrat'),
        ('148', 'Morocco'),
        ('149', 'Mozambique'),
        ('150', 'Myanmar'),
        ('151', 'Namibia'),
        ('152', 'Nauru'),
        ('153', 'Nepal'),
        ('154', 'Netherlands'),
        ('155', 'Netherlands Antilles'),
        ('156', 'New Caledonia'),
        ('157', 'New Zealand'),
        ('158', 'Nicaragua'),
        ('159', 'Niger'),
        ('160', 'Nigeria'),
        ('161', 'Niue'),
        ('162', 'Norfolk Island'),
        ('163', 'Northern Mariana Islands'),
        ('164', 'Norway'),
        ('165', 'Oman'),
        ('166', 'Pakistan'),
        ('167', 'Palau'),
        ('168', 'Palestinian Territory, Occupied'),
        ('169', 'Panama'),
        ('170', 'Papua New Guinea'),
        ('171', 'Paraguay'),
        ('172', 'Peru'),
        ('173', 'Philippines'),
        ('174', 'Pitcairn'),
        ('175', 'Poland'),
        ('176', 'Portugal'),
        ('177', 'Puerto Rico'),
        ('178', 'Qatar'),
        ('179', 'Reunion'),
        ('180', 'Romania'),
        ('181', 'Russian Federation'),
        ('182', 'Rwanda'),
        ('183', 'Saint Helena'),
        ('184', 'Saint Kitts And Nevis'),
        ('185', 'Saint Lucia'),
        ('186', 'Saint Pierre And Miquelon'),
        ('187', 'Saint Vincent And The Grenadines'),
        ('188', 'Samoa'),
        ('189', 'San Marino'),
        ('190', 'Sao Tome And Principe'),
        ('191', 'Saudi Arabia'),
        ('192', 'Senegal'),
        ('193', 'Serbia And Montenegro'),
        ('194', 'Seychelles'),
        ('195', 'Sierra Leone'),
        ('196', 'Singapore'),
        ('197', 'Slovakia'),
        ('198', 'Slovenia'),
        ('199', 'Solomon Islands'),
        ('200', 'Somalia'),
        ('201', 'South Africa'),
        ('202', 'South Georgia And The South Sandwich Islands'),
        ('203', 'Spain'),
        ('204', 'Sri Lanka'),
        ('205', 'Sudan'),
        ('206', 'Suriname'),
        ('207', 'Svalbard And Jan Mayen'),
        ('208', 'Swaziland'),
        ('209', 'Sweden'),
        ('210', 'Switzerland'),
        ('211', 'Syrian Arab Republic'),
        ('212', 'Taiwan, Province Of China'),
        ('213', 'Tajikistan'),
        ('214', 'Tanzania, United Republic Of'),
        ('215', 'Thailand'),
        ('216', 'Timor-Leste'),
        ('217', 'Togo'),
        ('218', 'Tokelau'),
        ('219', 'Tonga'),
        ('220', 'Trinidad And Tobago'),
        ('221', 'Tunisia'),
        ('222', 'Turkey'),
        ('223', 'Turkmenistan'),
        ('224', 'Turks And Caicos Islands'),
        ('225', 'Tuvalu'),
        ('226', 'Uganda'),
        ('227', 'Ukraine'),
        ('228', 'United Arab Emirates'),
        ('229', 'United Kingdom'),
        ('230', 'United States of America'),
        ('231', 'United States Minor Outlying Islands'),
        ('232', 'Uruguay'),
        ('233', 'Uzbekistan'),
        ('234', 'Vanuatu'),
        ('235', 'Venezuela'),
        ('236', 'Viet Nam'),
        ('237', 'Virgin Islands, British'),
        ('238', 'Virgin Islands, U.S.'),
        ('239', 'Wallis And Futuna'),
        ('240', 'Western Sahara'),
        ('241', 'Yemen'),
        ('242', 'Zambia'),
        ('243', 'Zimbabwe'),
    ]

    COMMUNICATION_MODE_CHOICES = [
        ('P', 'Physical'),
        ('E', 'Electronic'),
        ('M', 'Mobile'),
    ]
    
    BSE_RELATIONSHIP_CODE_CHOICES = [
        ('01', 'AUNT (Nominee Relationship)'),
        ('02', 'BROTHER-IN-LAW (Nominee Relationship)'),
        ('03', 'BROTHER (Nominee Relationship)'),
        ('04', 'DAUGHTER (Nominee Relationship)'),
        ('05', 'DAUGHTER-IN-LAW (Nominee Relationship)'),
        ('06', 'FATHER (Nominee & Guardian Relationship)'),
        ('07', 'FATHER-IN-LAW (Nominee Relationship)'),
        ('08', 'GRAND DAUGHTER (Nominee Relationship)'),
        ('09', 'GRAND FATHER (Nominee Relationship)'),
        ('10', 'GRAND MOTHER (Nominee Relationship)'),
        ('11', 'GRAND SON (Nominee Relationship)'),
        ('12', 'MOTHER-IN-LAW (Nominee Relationship)'),
        ('13', 'MOTHER (Nominee & Guardian Relationship)'),
        ('14', 'NEPHEW (Nominee Relationship)'),
        ('15', 'NIECE (Nominee Relationship)'),
        ('16', 'SISTER (Nominee Relationship)'),
        ('17', 'SISTER-IN-LAW (Nominee Relationship)'),
        ('18', 'SON (Nominee Relationship)'),
        ('19', 'SON-IN-LAW (Nominee Relationship)'),
        ('20', 'SPOUSE (Nominee Relationship)'),
        ('21', 'UNCLE (Nominee Relationship)'),
        ('22', 'OTHERS (Nominee Relationship)'),
        ('23', 'COURT APPOINTED LEGAL GUARDIAN (Guardian Relationship)'),
    ]
    
    KYC_TYPE_CHOICES = [
        ('K', 'KRA Compliant'),
        ('C', 'CKYC Compliant'),
        ('B', 'BIOMETRIC KYC'),
        ('E', 'Aadhaar Ekyc PAN'),
    ]
    
    Paperless_Flag = [
        ('P', 'Paper'),
        ('Z', 'paperless'),
    ]
    
    EMAIL_MOBILE_SELF_DECLARATION_CODE_CHOICES = [
        ('SE', 'Self'),
        ('SP', 'Spouse'),
        ('DC', 'Dependent Children'),
        ('DS', 'Dependent Siblings'),
        ('DP', 'Dependent Parents'),
        ('GD', 'Guardian'),
        ('PM', 'PMS'),
        ('CD', 'Custodian'),
        ('PO', 'POA'),
    ]
    
    NOMINATION_AUTHENTICATION_MODE_CHOICES = [
        ('W', 'Wet Signature'),
        ('E', 'eSign'),
        ('O', 'OTP Authentication'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True, blank=True)
    member_code     = models.CharField(max_length=20, null=True, blank=True)
    email 			= models.EmailField(blank=False, unique=True)
    mobile          = models.CharField(max_length=15, unique=True)
    mpin            = models.CharField(max_length=50)
    regn_type       = models.CharField(max_length=10, choices=REGN_TYPE,)
    param           = models.JSONField(null=True,)
    tax_status 		= models.CharField(max_length=2, choices=TAX_STATUS_CHOICES, verbose_name="Tax Status", null=True, blank=True)
    occupation_code = models.CharField(max_length=2, choices=OCCUPATION_CHOICES, verbose_name="Occupation Code",)
    holding_code 	= models.CharField(max_length=2, choices=CLIENT_HOLDING_CHOICES, verbose_name="Client Holding Code", null=True, blank=True)
    primary_holder_exempt_category 	= models.CharField(max_length=2, choices=PAN_EXEMPT_CATEGORY_CHOICES, verbose_name="Pan Exempt Category", null=True, blank=True)
    second_holder_exempt_category 	= models.CharField(max_length=2, choices=PAN_EXEMPT_CATEGORY_CHOICES, verbose_name="Second Pan Exempt Category", null=True, blank=True)
    third_holder_exempt_category 	= models.CharField(max_length=2, choices=PAN_EXEMPT_CATEGORY_CHOICES, verbose_name="Third Pan Exempt Category", null=True, blank=True)
    guardian_exempt_category 	    = models.CharField(max_length=2, choices=PAN_EXEMPT_CATEGORY_CHOICES, verbose_name="Guardian Exempt Category", null=True, blank=True)
    client_type 	                = models.CharField(max_length=1, choices=Client_Type, verbose_name="Client Type", null=True, blank=True)
    account_type_1 	                = models.CharField(max_length=2, choices=ACCOUNT_TYPE, verbose_name="Account Type One", null=True, blank=True)
    account_type_2 	                = models.CharField(max_length=2, choices=ACCOUNT_TYPE, verbose_name="Account Type Two", null=True, blank=True)
    account_type_3 	= models.CharField(max_length=2, choices=ACCOUNT_TYPE, verbose_name="Account Type Three", null=True, blank=True)
    account_type_4 	= models.CharField(max_length=2, choices=ACCOUNT_TYPE, verbose_name="Account Type Four", null=True, blank=True)
    account_type_5 	= models.CharField(max_length=2, choices=ACCOUNT_TYPE, verbose_name="Account Type Five", null=True, blank=True)
    div_pay_mode 	= models.CharField(max_length=2, choices=DIVIDEND_PAYMODE, verbose_name="Div Pay Mode", null=True, blank=True)
    state_code 	    = models.CharField(max_length=2, choices=STATE_CODE_CHOICES, verbose_name="State", null=True, blank=True)
    country_code 	= models.CharField(max_length=35, choices=COUNTRY_CODE_CHOICES, verbose_name="Country", null=True, blank=True)
    communication_mode 	    = models.CharField(max_length=2, choices=COMMUNICATION_MODE_CHOICES, verbose_name="Communication Mode", null=True, blank=True)
    nominee_1_relationship 	= models.CharField(max_length=2, choices=BSE_RELATIONSHIP_CODE_CHOICES, verbose_name="Nominee 1 Relationship", null=True, blank=True)
    nominee_2_relationship 	= models.CharField(max_length=2, choices=BSE_RELATIONSHIP_CODE_CHOICES, verbose_name="Nominee 2 Relationship", null=True, blank=True)
    nominee_3_relationship 	= models.CharField(max_length=2, choices=BSE_RELATIONSHIP_CODE_CHOICES, verbose_name="Nominee 3 Relationship", null=True, blank=True)
    guardian_relationship 	= models.CharField(max_length=2, choices=BSE_RELATIONSHIP_CODE_CHOICES, verbose_name="Guardian Relationship", null=True, blank=True)
    primary_holder_kyc_type = models.CharField(max_length=1, choices=KYC_TYPE_CHOICES, verbose_name="Primary Holder Kyc Type", null=True, blank=True)
    second_holder_kyc_type 	= models.CharField(max_length=1, choices=KYC_TYPE_CHOICES, verbose_name="Second Holder Kyc Type", null=True, blank=True)
    third_holder_kyc_type 	= models.CharField(max_length=1, choices=KYC_TYPE_CHOICES, verbose_name="Third Holder Kyc Type", null=True, blank=True)
    guardian_holder_kyc_type 	        = models.CharField(max_length=1, choices=KYC_TYPE_CHOICES, verbose_name="Gaurdian Holder Kyc Type", null=True, blank=True)
    paperless_flag 	                    = models.CharField(max_length=1, choices=Paperless_Flag, verbose_name="Paperless Flag", null=True, blank=True)
    filler_1_mobile_declaration_flag 	= models.CharField(max_length=2, choices=EMAIL_MOBILE_SELF_DECLARATION_CODE_CHOICES, verbose_name="Filler 1 Mobile Declaration Flag", null=True, blank=True)
    filler_2_email_declaration_flag 	= models.CharField(max_length=2, choices=EMAIL_MOBILE_SELF_DECLARATION_CODE_CHOICES, verbose_name="Filler 1 Email Declaration Flag", null=True, blank=True)
    second_holder_email_declaration 	= models.CharField(max_length=2, choices=EMAIL_MOBILE_SELF_DECLARATION_CODE_CHOICES, verbose_name="Second Holder Email Declaration", null=True, blank=True)
    second_holder_mobile_declaration 	= models.CharField(max_length=2, choices=EMAIL_MOBILE_SELF_DECLARATION_CODE_CHOICES, verbose_name="Second Holder Mobile Declaration", null=True, blank=True)
    third_holder_mobile_declaration 	= models.CharField(max_length=2, choices=EMAIL_MOBILE_SELF_DECLARATION_CODE_CHOICES, verbose_name="Third Holder Mobile Declaration", null=True, blank=True)
    third_holder_email_declaration 	    = models.CharField(max_length=2, choices=EMAIL_MOBILE_SELF_DECLARATION_CODE_CHOICES, verbose_name="Third Holder Email Declaration", null=True, blank=True)
    nomination_auth_mode 	            = models.CharField(max_length=1, choices=NOMINATION_AUTHENTICATION_MODE_CHOICES, verbose_name="Nomination Auth Mode", null=True, blank=True)
    
    filler_1        = models.CharField(max_length=50, null=True, blank=True)
    filler_2        = models.CharField(max_length=50, null=True, blank=True)
    otp 		    = models.CharField(max_length=10, null=True, blank=True)
    Signature_image = models.ImageField(upload_to="Signature/", null=True, blank=True)
    Term_conditions = models.BooleanField(default=True, null=True, blank=True)
    is_submit       = models.BooleanField(default=False, null=True, blank=True)
    created_time 	= models.DateTimeField(auto_now_add=True)
    utimestamp 		= models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{str(self.user)}"

class Fatca(models.Model):

    DATA_SRC_CHOICES = [
        ('P', 'Physical'),
        ('E', 'Electronic'),
    ]

    ADDRESS_CHOICES = [
        ('1', 'Residential or Business'),
        ('2', 'Residential'),
        ('3', 'Business'),
        ('4', 'Registered Office'),
        ('5', 'Unspecified'),
    ]

    FLAG_CHOICES = [
        ('Y', 'Yes'), 
        ('N', 'No'), 
        ('R', 'Relative')
    ]

    OCCUPATIONS_TYPES_CHOICES = [
        ('S', 'Service'), 
        ('B', 'Business'), 
        ('O', 'Others'), 
        ('X', 'Not Categorized')
    ]

    GENDER_CHOICES = [
        ('M', 'Male'), 
        ('F', 'Female'), 
        ('O', 'Other')
    ]

    EXCH_CHOICES = [
        ('B', 'BSE'), 
        ('N', 'NSE'), 
        ('O', 'Others')
    ]

    STATUS_CHOICES = [
        ('N', 'This value should be updated for first time'),
        ('C', 'This Value should be provided for change in already provided information'),
    ]

    UBO_APPLICATIONS_CHOICE = [
        ('Y', 'Yes'), 
        ('N', 'No'),
    ]

    user           = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    agent          = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True, blank=True)
    param          = models.JSONField(null=True)
    pan_number     = models.CharField(max_length=10, unique=True, null=True, blank=True)
    invester_name  = models.CharField(max_length=70)
    dob            = models.DateField(null=True, blank=True)
    tax_status     = models.CharField(max_length=3, choices=TAX_STATUS_CHOICES)
    data_src       = models.CharField(max_length=3, choices=DATA_SRC_CHOICES)
    address_type   = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    applications_type = models.CharField(max_length=60)
    tpin1       = models.CharField(max_length=20)
    srce_wealt  = models.CharField(max_length=3)
    pep_flag    = models.CharField(max_length=2, choices=FLAG_CHOICES, null=True, blank=True)
    occupation_code  = models.CharField(max_length=2, choices=OCCUPATION_CHOICES)
    occupation_Type  = models.CharField(max_length=1, choices=OCCUPATIONS_TYPES_CHOICES)
    exch_name        = models.CharField(max_length=2, choices=EXCH_CHOICES)
    ubo_appl         = models.CharField(max_length=2, choices=UBO_APPLICATIONS_CHOICE)
    ubo_count        = models.CharField(max_length=3, null=True, blank=True)
    ubo_name         = models.CharField(max_length=70, null=True, blank=True)
    ubo_pan          = models.CharField(max_length=10, null=True, blank=True)
    ubo_add_ty       = models.CharField(max_length=2, choices=ADDRESS_CHOICES, null=True, blank=True)
    ubo_gender       = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    ubo_fr_nam       = models.CharField(max_length=50, null=True, blank=True)
    ubo_occ          = models.CharField(max_length=2, choices=OCCUPATION_CHOICES, null=True, blank=True)
    ubo_occ_ty       = models.CharField(max_length=2, choices=OCCUPATIONS_TYPES_CHOICES, null=True, blank=True)
    ubo_code         = models.CharField(max_length=3, null=True, blank=True)
    aadhaar_rp       = models.CharField(max_length=30, null=True, blank=True)
    new_change       = models.CharField(max_length=2, choices=STATUS_CHOICES)
    log_name         = models.CharField(max_length=30, null=True, blank=True)
    UBO_EXCH         = models.CharField(max_length=4, choices=EXCH_CHOICES, null=True, blank=True)
    filler1          = models.CharField(max_length=30, null=True, blank=True)
    filler2          = models.CharField(max_length=30, null=True, blank=True)
    api_data         = models.JSONField()
    created_time 	 = models.DateTimeField(auto_now_add=True)
    utimestamp 		 = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.invester_name
    
class Mandate(models.Model):
    MANDATE_TYPE_CHOICE = [
        ('X', 'XSIP'),
        ('I', 'ISIP'),
        ('N', 'Net Banking')
    ]
    
    user         = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    agent        = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True, blank=True)
    mandate_id   = models.CharField(max_length=10)    
    client_code  = models.CharField(max_length=10)
    amount       = models.CharField(max_length=100)
    mandate_type = models.CharField(max_length=1, choices=MANDATE_TYPE_CHOICE)
    account_no   = models.CharField(max_length=20)
    account_type = models.CharField(max_length=2, choices=ACCOUNT_TYPE)
    ifsc_code    = models.CharField(max_length=11)
    misc_code    = models.CharField(max_length=9, null=True, blank=True)
    start_date   = models.DateField()
    end_date     = models.DateField()
    api_data     = models.JSONField()
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    def __str__(self):
          return self.client_code
    
class Enach(models.Model):
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    agent        = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True, blank=True)
    client_code  = models.CharField(max_length=10)
    mandate_id   = models.CharField(max_length=25)
    api_data     = models.JSONField()
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_code
    
class AMCList(models.Model):
    AMC_list_file = models.FileField(upload_to="AMC list/")
    param = models.JSONField(null=True, blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

class XSIPTransaction(models.Model):
    GOAL_TYPE_CHOICES = [
        ("01", "Kids Marriage"),
        ("02", "Retirement Planning"),
        ("03", "Kids’ Education"),
        ("04", "Tax Savings"),
        ("05", "Dream House"),
        ("06", "Dream Car"),
        ("07", "Dream Vacation"),
        ("08", "Others"),
    ]

    XSIP_TYPE_CHOICES = [
        ("01", "Regular XSIP"),
        ("02", "Power XSIP"),
        ("03", "Freedom XSIP"),
        ("07", "MITRA XSIP"),
        ("08", "SAMPOORNA XSIP"),
        ("09", "WHITEOAK XSIP"),
    ]

    REGISTRATION_TYPE_CHOICES = [
        ('ISIP', 'ISIP'),
        ('XSIP', 'XSIP'),
    ]

    YN_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]

    DP_TRANSACTION_MODE_CHOICES = [
        ('C', 'CDSL'),
        ('N', 'NSDL'),
        ('P', 'PHYSICAL'),
    ]

    TRANSMODE_CHOICES = [
        ('D', 'Demat'),
        ('P', 'Physical'),
    ]

    FREQUENCY_TYPE_CHOICES = [
        ('MONTHLY', 'Monthly'),
        ('QUARTERLY', 'Quarterly'),
        ('WEEKLY', 'Weekly'),
    ]

    STATUS_CHOICES=[
        ('INACTIVE', 'Inactive'), 
        ('ACTIVE', 'Active'), 
        ('CANCELLED', 'Cancelled')
    ]

    CEASE_BSE_CODE_CHOICES = [
        ("01", "Non availability of Funds"),
        ("02", "Scheme not performing"),
        ("03", "Service issue"),
        ("04", "Load Revised"),
        ("05", "Wish to invest in other schemes"),
        ("06", "Change in Fund Manager"),
        ("07", "Goal Achieved"),
        ("08", "Not comfortable with market volatility"),
        ("09", "Will be restarting SIP after few months"),
        ("10", "Modifications in bank/mandate/date etc"),
        ("11", "I have decided to invest elsewhere"),
        ("12", "This is not the right time to invest"),
        ("13", "Others (pls specify the reason)"),
    ]

    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    agent       = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True, blank=True)
    scheme_code = models.CharField(max_length=20)
    client_code = models.CharField(max_length=20)
    xsipregid   = models.CharField(max_length=20, blank=True, null=True)
    int_ref_no = models.CharField(max_length=50, blank=True, null=True)
    trans_mode = models.CharField(max_length=5, choices=TRANSMODE_CHOICES)
    dp_trans_mode = models.CharField(max_length=5, choices=DP_TRANSACTION_MODE_CHOICES)
    start_date = models.DateField()
    frequency_type = models.CharField(max_length=20, choices=FREQUENCY_TYPE_CHOICES)
    frequency_allowed = models.IntegerField()
    installments_amount = models.DecimalField(max_digits=10, decimal_places=2)
    no_of_installments = models.IntegerField()
    remarks = models.CharField(max_length=100, blank=True, null=True)
    folio_no = models.CharField(max_length=50, blank=True, null=True)
    first_order_flag = models.CharField(max_length=5, choices=YN_CHOICES)
    sub_br_code = models.CharField(max_length=20, blank=True, null=True)
    euin = models.CharField(max_length=20, blank=True, null=True)
    euin_flag = models.CharField(max_length=5, choices=YN_CHOICES)
    dpc = models.CharField(max_length=5, choices=YN_CHOICES)
    sub_broker_arn = models.CharField(max_length=50, blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    regn_type = models.CharField(max_length=10, choices=REGISTRATION_TYPE_CHOICES)
    brokerage = models.CharField(max_length=50, blank=True, null=True)
    mandate_id = models.CharField(max_length=20)
    xsip_type = models.CharField(max_length=10, choices=XSIP_TYPE_CHOICES)
    target_scheme = models.CharField(max_length=50, blank=True, null=True)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    goal_type = models.CharField(max_length=50, choices=GOAL_TYPE_CHOICES, blank=True, null=True)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    filler1 = models.CharField(max_length=50, blank=True, null=True)
    filler2 = models.CharField(max_length=50, blank=True, null=True)
    filler3 = models.CharField(max_length=50, blank=True, null=True)
    filler4 = models.CharField(max_length=50, blank=True, null=True)
    filler5 = models.CharField(max_length=50, blank=True, null=True)
    filler6 = models.CharField(max_length=50, blank=True, null=True)
    filler7 = models.CharField(max_length=50, blank=True, null=True)
    filler8 = models.CharField(max_length=50, blank=True, null=True)
    filler9 = models.CharField(max_length=50, blank=True, null=True)
    filler10 = models.CharField(max_length=50, blank=True, null=True)
    cease_bse_code = models.CharField(max_length=10, choices=CEASE_BSE_CODE_CHOICES, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='INACTIVE', blank=True, null=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"XSIP Transaction - {self.client_code}"
    
class AMCCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='amc_cart')
    scheme_code = models.CharField(max_length=100)
    scheme_name = models.CharField(max_length=500)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.scheme_code}"