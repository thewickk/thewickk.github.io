from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class RegisterServer(FlaskForm):
    hostname = StringField(
        'Hostname',
        validators=[
            DataRequired(message='Please enter a hostname'),
        ],
        render_kw={'placeholder': 'Please enter a Hostname'}
    )
    processor = SelectField(
        'CPU',
        validators=[
            DataRequired(message='Please select a CPU')
        ],
        choices=[
            ('', 'Please Select A CPU'),
            ('Xeon E5603 Westmere-EP', 'Xeon E5603 Westmere-EP'),
            ('i7 990x Gulftown', 'i7 990x Gulftown'),
            ('Intel Pentium 4 3200MHz', 'Intel Pentium 4 3200MHz'),
            ('i7 965 Bloomfield', 'i7 965 Bloomfield'),
            ('i7 4770 Haswell', 'i7 4770 Haswell'),
            ('i7 6700k Skylake', 'i7 6700k Skylake'),
            ('i7 8700k Coffee Lake', 'i7 8700k Coffee Lake'),
            ('Other', 'Other'),
            ('N/A', 'N/A')
        ],
        default='N/A'
    )
    motherboard = SelectField(
        'Motherboard',
        validators=[
            DataRequired(message='Please select a motherboard')
        ],
        choices=[
            ('', 'Please Select A Motherboard'),
            ('EVGA X58 Classified', 'EVGA X58 Classified'),
            ('ASRock Z170M PRO4S', 'ASRock Z170M PRO4S'),
            ('ASUS Z97-WS', 'ASUS Z97-WS'),
            ('Supermicro X10SAT', 'Supermicro X10SAT'),
            ('ASUS Prime Z370', 'ASUS Prime Z370'),
            ('ASUS P6X58D-E', 'ASUS P6X58D-E'),
            ('ASRock Z87 Extreme', 'ASRock Z87 Extreme'),
            ('Other', 'Other'),
            ('N/A', 'N/A')
        ],
        default='N/A'
    )
    memory_type = SelectField(
        'Memory Type',
        validators=[
            DataRequired(message='Please select a memory type')
        ],
        choices=[
            ('', 'Please Select Memory Type'),
            ('G.Skill DDR4', 'G.Skill DDR4'),
            ('G.Skill DDR3', 'G.Skill DDR3'),
            ('Kingston DDR4', 'Kingston DDR4'),
            ('Kingston DDR3', 'Kingston DDR3'),
            ('Corsair DDR4', 'Corsair DDR4'),
            ('Corsair DDR3', 'Corsair DDR3'),
            ('Other', 'Other'),
            ('N/A', 'N/A')
        ],
        default='N/A'
    )
    memory_qty = SelectField(
        'Memory Quantity',
        validators=[
            DataRequired(message='Please select a memory quantity')
        ],
        choices=[
            ('', 'Please Select Memory Quantity'),
            ('2GB', '2GB'),
            ('4GB', '4GB'),
            ('8GB', '8GB'),
            ('12GB', '12GB'),
            ('16GB', '16GB'),
            ('32GB', '32GB'),
            ('Other', 'Other'),
            ('N/A', 'N/A')
        ],
        default='N/A'
    )

    gpu_one = SelectField(
        'GPU One',
        validators=[
            DataRequired(message='Please select GPU one')
        ],
        choices=[
            ('', 'Please Select GPU One'),
            ('Nvidia GT 610', 'Nvidia GT 610'),
            ('Nvidia GT 710', 'Nvidia GT 710'),
            ('Nvidia GTX 295', 'Nvidia GTX 295'),
            ('Nvidia GTX 780', 'Nvidia GTX 780'),
            ('Nvidia GTX 780Ti', 'Nvidia GTX 780Ti'),
            ('Nvidia NVS 810', 'Nvidia NVS 810'),
            ('Nvidia GTX 980', 'Nvidia GTX 980'),
            ('Nvidia GTX 980Ti', 'Nvidia GTX 980Ti'),
            ('Nvidia GTX 1080', 'Nvidia GTX 1080'),
            ('Nvidia GTX 1080Ti', 'Nvidia GTX 1080Ti'),
            ('Other', 'Other'),
            ('N/A', 'N/A')
        ],
        default='N/A'
    )
    gpu_two = SelectField(
        'GPU Two',
        choices=[
            ('', 'Please Select GPU Two'),
            ('Nvidia GT 610', 'Nvidia GT 610'),
            ('Nvidia GT 710', 'Nvidia GT 710'),
            ('Nvidia GTX 295', 'Nvidia GTX 295'),
            ('Nvidia GTX 780', 'Nvidia GTX 780'),
            ('Nvidia GTX 780Ti', 'Nvidia GTX 780Ti'),
            ('Nvidia NVS 810', 'Nvidia NVS 810'),
            ('Nvidia GTX 980', 'Nvidia GTX 980'),
            ('Nvidia GTX 980Ti', 'Nvidia GTX 980Ti'),
            ('Nvidia GTX 1080', 'Nvidia GTX 1080'),
            ('Nvidia GTX 1080Ti', 'Nvidia GTX 1080Ti'),
            ('Other', 'Other'),
            ('N/A', 'N/A')
        ],
        default='N/A'
    )
    storage = SelectField(
        'Storage Device',
        validators=[
            DataRequired(message='Please select a storage device')
        ],
        choices=[
            ('', 'Please Select Storage Type'),
            ('WD 600GB HDD', 'WD 600GB HDD'),
            ('Intel 250GB SSD', 'Intel 250GB SSD'),
            ('Samsung 850 EVO 250GB SSD', 'Samsung 850 EVO 250GB SSD'),
            ('Samsung 850 EVO 500GB SSD', 'Samsung 850 EVO 500GB SSD'),
            ('Samsung 950 Pro 250GB M.2', 'Samsung 950 Pro 250GB M.2'),
            ('Samsung 950 Pro 500GB M.2', 'Samsung 950 Pro 500GB M.2'),
            ('Samsung 960 PRO 1TB M.2', 'Samsung 960 PRO 1TB M.2'),
            ('Other', 'Other'),
            ('N/A', 'N/A')
        ],
        default='N/A'
    )
    operating_system = SelectField(
        'Operating System',
        validators=[
            DataRequired(message='Please select an Operating System')
        ],
        choices=[
            ('', 'Please Select Operating System'),
            ('Windows XP Pro SP3', 'Windows XP Pro SP3'),
            ('Windows 7 Pro 64-bit', 'Windows 7 Pro 64-bit'),
            ('Windows 10 Pro 64-bit', 'Windows 10 Pro 64-bit'),
            ('Other', 'Other'),
            ('N/A', 'N/A')
        ],
        default='N/A'
    )
    mac_addr_one = StringField(
        'MAC Address One',
        validators=[
            DataRequired(message='Please enter a MAC Address')
        ],
        default='N/A',
        render_kw={'placeholder': 'Format: XX-XX-XX-XX-XX-XX or None for No '
                                  'MAC'}
    )
    mac_addr_two = StringField(
        'MAC Address Two',
        validators=[
            DataRequired(message='Please enter a MAC Address')
        ],
        default = 'N/A',
        render_kw={'placeholder': 'Format: XX-XX-XX-XX-XX-XX or None for No '
                                  'MAC'}
    )
    build_date = StringField(
        'Build Date',
        validators=[
            DataRequired(message='Please enter a build date')
        ],
        default='N/A',
        render_kw={'placeholder': 'Please enter build date or N/A if unknown'}
    )
    upgrade_status = SelectField(
        'Upgrade Status',
        validators=[
            DataRequired(message='Please enter current build status')
        ],
        choices=[
            ('', 'Please select upgrade status'),
            ('Legacy Equipment', 'Legacy Equipment'),
            ('Pending/Needs Upgrade', 'Pending/Needs Upgrade'),
            ('Upgraded', 'Upgraded')
        ],
        default='Pending/Needs Upgrade',
        render_kw={'placeholder': 'Enter current upgrade status'}
    )
    simulator_id = SelectField(
        'Assign Server to a Simulator',
        choices=[
            (1, 'Embraer E175'),
            (2, 'Boeing 737 MAX'),
            (3, 'Sikorsky S-76'),
            (4, 'Airbus A320'),
            (5, 'Boeing 777'),
            (6, 'Redbird Cessna C172'),
            (7, 'Microjet'),
            (8, 'Redbird King Air')
        ],
        coerce=int
    )
    submit = SubmitField(
        'Create Server'
    )


class AllocateServer(FlaskForm):
    server = SelectField(
        'Allocate To Sim',
        validators=[
            DataRequired()
        ],
        coerce=int
    )

    submit = SubmitField(
        'Allocate Server'
    )
