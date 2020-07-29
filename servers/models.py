from application import db


class Server(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    hostname = db.Column(db.String(255), nullable=False)
    processor = db.Column(db.String(255), nullable=False)
    motherboard = db.Column(db.String(255), nullable=False)
    memory_type = db.Column(db.String(255), nullable=False)
    memory_qty = db.Column(db.String(255), nullable=False)
    gpu_one = db.Column(db.String(255), nullable=False)
    gpu_two = db.Column(db.String(255), nullable=True)
    storage = db.Column(db.String(255), nullable=False)
    operating_system = db.Column(db.String(255), nullable=False)
    mac_addr_one = db.Column(db.String(255), nullable=False)
    ip_addr_one = db.Column(db.String(255), default='No Assigned IP')
    mac_addr_two = db.Column(db.String(255))
    ip_addr_two = db.Column(db.String(255), default='No Assigned IP')
    build_date = db.Column(db.String(255), default='unknown')
    upgrade_status = db.Column(db.String(255), default='Pending')
    simulator_id = db.Column(db.Integer(), db.ForeignKey('simulator.id'))
    network_addresses = db.relationship(
        'Network',
        backref='server',
        lazy='dynamic'
    )

    # @classmethod
    # def create_server(cls, hostname, processor, motherboard, memory_type,
    #                   memory_qty, gpu_one, gpu_two, storage, operating_system,
    #                   mac_one, ip_one, mac_two, ip_two, build_date,
    #                   upgrade_status, simulator_id):
    #     server = cls(
    #         hostname=hostname,
    #         processor=processor,
    #         motherboard=motherboard,
    #         memory_type=memory_type,
    #         memory_qty=memory_qty,
    #         gpu_one=gpu_one,
    #         gpu_two=gpu_two,
    #         storage=storage,
    #         operating_system=operating_system,
    #         mac_addr_one=mac_one,
    #         ip_one=ip_one,
    #         mac_addr_two=mac_two,
    #         ip_two=ip_two,
    #         build_date=build_date,
    #         upgrade_status=upgrade_status,
    #         simulator_id=simulator_id
    #     )
    #
    #     db.session.add(server)
    #     db.session.commit()
    #     return server
