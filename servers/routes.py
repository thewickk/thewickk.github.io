# application/servers/routes.py

from application.servers import servers
from flask import render_template, request, flash, redirect, url_for
from application import db
from flask_login import login_required
from application.servers.models import Server
from application.simulators.models import Simulator
from application.servers.forms import RegisterServer, AllocateServer
from application.networks.models import Network


@servers.route('/servers/')
def all_servers():
    servers = Server.query.filter().order_by(
        Server.simulator_id.asc())
    return render_template('servers.html', servers=servers)


@servers.route('/server/<int:server_id>')
def server_info(server_id):
    server = Server.query.get(server_id)
    ip_address = Network.query.filter_by(server_id=server.id).first()
    server_ip_one = server.ip_addr_one
    server_ip_two = server.ip_addr_two
    ip_one_id = Network.query.filter_by(address=server_ip_one).first()
    ip_two_id = Network.query.filter_by(address=server_ip_two).first()
    server_ips = list(server.network_addresses)
    sim = Simulator.query.filter_by(id=server.simulator_id).first()
    return render_template('server_info.html', server=server, sim=sim,
                           ip_one_id=ip_one_id,
                           ip_two_id=ip_two_id)


@servers.route('/server/add_server/', methods=['GET', 'POST'])
@login_required
def add_server():
    form = RegisterServer()
    if form.validate_on_submit():
        sim_id = Simulator.query.filter_by(id=form.simulator_id.data).first()
        server = Server(
            hostname=form.hostname.data,
            processor=form.processor.data,
            motherboard=form.motherboard.data,
            memory_type=form.memory_type.data,
            memory_qty=form.memory_qty.data,
            gpu_one=form.gpu_one.data,
            gpu_two=form.gpu_two.data,
            storage=form.storage.data,
            operating_system=form.operating_system.data,
            mac_addr_one=form.mac_addr_one.data,
            mac_addr_two=form.mac_addr_two.data,
            build_date=form.build_date.data,
            upgrade_status=form.upgrade_status.data,
            simulator_id=form.simulator_id.data
        )
        db.session.add(server)
        db.session.commit()
        flash('Server successfully created')
        return redirect(url_for('main.sim_page', simulator_id=sim_id.id))
    return render_template('add_server.html', form=form)


# TODO Make this work!!
@servers.route('/server/add_new_server_to_sim/<int:sim_id>/', methods=['GET', 'POST'])
@login_required
def add_new_server_to_sim(sim_id):
    form = RegisterServer()
    if form.validate_on_submit():
        simulator_id = Simulator.query.filter_by(id=sim_id).first()

        server = Server(
            hostname=form.hostname.data,
            processor=form.processor.data,
            motherboard=form.motherboard.data,
            memory_type=form.memory_type.data,
            memory_qty=form.memory_qty.data,
            gpu_one=form.gpu_one.data,
            gpu_two=form.gpu_two.data,
            storage=form.storage.data,
            operating_system=form.operating_system.data,
            mac_addr_one=form.mac_addr_one.data,
            mac_addr_two=form.mac_addr_two.data,
            build_date=form.build_date.data,
            upgrade_status=form.upgrade_status.data,
            simulator_id=form.populate_obj(simulator_id)
        )
        db.session.add(server)
        db.session.commit()
        flash('Server successfully created')
        return redirect(url_for('servers.add_server'))
    return render_template('add_server.html', form=form)


@servers.route('/server/remove/<int:server_id>', methods=['GET', 'POST'])
@login_required
def remove_server(server_id):
    server = Server.query.get(server_id)
    server_ips = list(server.network_addresses)
    sim = Simulator.query.filter_by(id=server.simulator_id).first()
    if request.method == 'POST':
        server.simulator_id = None
        db.session.commit()
        return redirect(url_for('servers.server_info', server_id=server_id))
    return render_template('remove_server.html', server=server,
                           server_id=server_id, sim=sim)


@servers.route('/server/delete/<int:server_id>', methods=['GET', 'POST'])
@login_required
def delete_server(server_id):
    server = Server.query.get(server_id)
    sim = Simulator.query.filter_by(id=server.simulator_id).first()
    if request.method == 'POST':
        db.session.delete(server)
        db.session.commit()
        flash('Server deleted')
        return redirect(url_for('main.home'))
    return render_template('delete_server.html', server=server,
                           server_id=server.id, sim=sim)


@servers.route('/allocate_server/<int:svr_id>', methods=['GET', 'POST'])
@login_required
def allocate_server(svr_id):
    server = Server.query.filter_by(id=svr_id).first()
    form = AllocateServer(form_name="AllocateServer")
    form.server.choices = [(row.id, row.name) for row in Simulator.query.all()]
    if form.validate_on_submit():
        server.simulator_id = form.server.data
        db.session.commit()
        flash('Server Successfully Added to Simulator')
        return redirect(url_for('main.sim_page', simulator_id=form.server.data))
    return render_template('add_server.html', form=form)


@servers.route('/server/remove_ip_one/<int:server_id>/<int:ip_id>',
               methods=['GET', 'POST'])
@login_required
def remove_ip_one(server_id, ip_id):
    server = Server.query.filter_by(id=server_id).first()
    ip_address = Network.query.filter_by(id=ip_id).first()
    if request.method == 'POST':
        ip_address.server_id = None
        server.ip_addr_one = 'No Assigned IP'
        db.session.commit()
        return redirect(url_for('servers.server_info', server_id=server_id))
    return render_template('remove_ip_one.html', server=server,
                           ip_address=ip_address)


@servers.route('/server/remove_ip_two/<int:server_id>/<int:ip_id>',
               methods=['GET','POST'])
@login_required
def remove_ip_two(server_id, ip_id):
    server = Server.query.filter_by(id=server_id).first()
    ip_address = Network.query.filter_by(id=ip_id).first()
    server_ips = list(server.network_addresses)
    if request.method == 'POST':
        ip_address.server_id = None
        server.ip_addr_two = 'No Assigned IP'
        db.session.commit()
        return redirect(url_for('servers.server_info', server_id=server_id))
    return render_template('remove_ip_two.html', server=server,
                           ip_address=ip_address)


@servers.route('/server/direct_to_sim/<int:svr_id>', methods=['POST'])
@login_required
def direct_to_sim(svr_id):
    return "Testing"


# TODO - Add this button to servrs.all_servers route
@servers.route('/servers/avail_servers/')
@login_required
def avail_servers():
    avail = Server.query.filter().order_by(Server.id.asc()).filter_by(
        simulator_id=None)
    return render_template('avail_servers.html', avail=avail)


@servers.route('/server/x-plane_build/')
def x_plane_build():
    return render_template('x-plane_build.html')


@servers.route('/server/pdu_build/')
def pdu_build():
    return render_template('pdu_build.html')


@servers.route('/server/input_output_build/')
def input_output_build():
    return render_template('input_output_build.html')


@servers.route('/server/workstation_build/')
def workstation_build():
    return render_template('workstation_build.html')


@servers.route('/server/smartroom_build/')
def smartroom_build():
    return render_template('smartroom_build.html')
