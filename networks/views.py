# PROJECT/NETWORK/VIEWS.PY
from project.networks import networks_blueprint
from flask import render_template, request, current_app, flash, redirect, url_for, jsonify
from project import db
from project.office.models import Office
from project.networks.models import Network
from project.devices.models import Device
from project.networks.forms import AllocateIP
from flask_login import login_required


@networks_blueprint.route('/network_home')
def network_home():
    return render_template('network_home.html')

@networks_blueprint.route('/ip_address/<ip_address>/JSON/')
def single_ip_json(ip_address):
    ip = Network.query.filter_by(address=ip_address).first()
    return jsonify(Network=[ip.serialize])


@networks_blueprint.route('/csf_networks')
def csf_networks():
    page = request.args.get('page', 1, type=int)
    ip_addresses = Network.query.paginate(page, current_app.config.get('ADDRESSES_PER_PAGE'), False)
    return render_template('networks.html', ip_addresses=ip_addresses)


@networks_blueprint.route('/71_network')
def seventy_one_net():
    page = request.args.get('page', 1, type=int)
    ip_addresses = Network.query.filter(Network.address.like("%10.0.71.%")).order_by(Network.id.asc()). \
        paginate(page, current_app.config.get('ADDRESSES_PER_PAGE'), False)
    return render_template('71_network.html', ip_addresses=ip_addresses)


@networks_blueprint.route('/71_network/JSON')
def seventy_one_net_json():
    ip_addresses = Network.query.filter(Network.address.like("%10.0.71.%")).order_by(Network.id.asc())
    return jsonify(Network=[i.serialize for i in ip_addresses])

@networks_blueprint.route('/72_network')
def seventy_two_net():
    page = request.args.get('page', 1, type=int)
    ip_addresses = Network.query.filter(Network.address.like("%10.0.72.%")).order_by(Network.id.asc()). \
        paginate(page, current_app.config.get('ADDRESSES_PER_PAGE'), False)
    return render_template('72_network.html', ip_addresses=ip_addresses)

@networks_blueprint.route('/72_network/JSON')
def seventy_two_net_json():
    ip_addresses = Network.query.filter(Network.address.like("%10.0.72.%")).order_by(Network.id.asc())
    return jsonify(Network=[i.serialize for i in ip_addresses])


@networks_blueprint.route('/73_network')
def seventy_three_net():
    page = request.args.get('page', 1, type=int)
    ip_addresses = Network.query.filter(Network.address.like("%10.0.73.%")).order_by(Network.id.asc()). \
        paginate(page, current_app.config.get('ADDRESSES_PER_PAGE'), False)
    return render_template('73_network.html', ip_addresses=ip_addresses)

@networks_blueprint.route('/73_network/JSON')
def seventy_three_net_json():
    ip_addresses = Network.query.filter(Network.address.like("%10.0.73.%")).order_by(Network.id.asc())
    return jsonify(Network=[i.serialize for i in ip_addresses])

@networks_blueprint.route('/74_network')
def seventy_four_net():


    page = request.args.get('page', 1, type=int)
    ip_addresses = Network.query.filter(Network.address.like("%10.0.74.%")).order_by(Network.id.asc()). \
        paginate(page, current_app.config.get('ADDRESSES_PER_PAGE'), False)
    return render_template('74_network.html', ip_addresses=ip_addresses)

@networks_blueprint.route('/74_network/JSON')
def seventy_four_net_json():
    ip_addresses = Network.query.filter(Network.address.like("%10.0.74.%")).order_by(Network.id.asc())
    return jsonify(Network=[i.serialize for i in ip_addresses])


@networks_blueprint.route('/75_network')
def seventy_five_net():
    page = request.args.get('page', 1, type=int)
    ip_addresses = Network.query.filter(Network.address.like("%10.0.75.%")).order_by(Network.id.asc()). \
        paginate(page, current_app.config.get('ADDRESSES_PER_PAGE'), False)
    return render_template('75_network.html', ip_addresses=ip_addresses)


@networks_blueprint.route('/allocate_ip/<int:ip_id>', methods=['GET', 'POST'])
@login_required
def allocate_ip(ip_id):
    ip_address = Network.query.filter_by(id=ip_id).first_or_404()
    form = AllocateIP()
    form.allocate_ip.choices = [(row.id, row.hostname) for row in
                               Device.query.order_by(Device.id.asc())]
    if form.validate_on_submit():
        ip_address.device_id = form.allocate_ip.data
        db.session.commit()
        flash("IP Added")
        return redirect(url_for('devices.device',
                                device_id=form.allocate_ip.data,
                                ip_address=ip_address))
    return render_template('allocate_ip.html', form=form,
                           ip_address=ip_address)
