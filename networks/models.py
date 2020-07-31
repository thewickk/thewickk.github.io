# project/networks/models.py
from project import db
from project.devices.models import Device


class Network(db.Model):
    __tablename__ = 'network'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(32))
    network_id = db.Column(db.String(64))
    reserved_id = db.Column(db.Integer, db.ForeignKey('office.id'))
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))

    # If IP is connected to a device, return string representation of the hostname of the device the IP is connected to.
    # This is useful for displaying hostnames in tags next to the IP on the Network and Office Info pages
    def __repr__(self):
        if self.device_id != None:
            device = Device.query.get(self.device_id)
            hostname = device.hostname
        return f"{hostname}"

    # Create network data for our JSON endpoint
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        if self.network_id == 1:
            office_group = 'Accounting'
        elif self.network_id == 2:
            office_group = 'IT'
        elif self.network_id == 3:
            office_group = 'Administration'
        elif self.network_id == 4:
            office_group = 'CEO'
        elif self.network_id == 5:
            office_group = 'Developers'
        else:
            office_group = 'IP is not part of an office group'

        if self.device_id is not None:
            device = Device.query.get(self.device_id)
            hostname = device.hostname
        else:
            hostname = 'IP currently is not associated with a device'
        return {
            'address': self.address,
            'office_group': office_group,
            'host_device': hostname
        }
