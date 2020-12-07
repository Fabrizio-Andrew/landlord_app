class Unit extends React.Component {

    constructor(props) {
        super(props);
 
        this.state = {
            unit: this.props.unit,
            showcontent: this.props.showcontent,
            showeditform: this.props.showeditform,
            newunit: this.props.newunit
        }

        this.edit_click = this.edit_click.bind(this);
        this.DeleteUnit = this.DeleteUnit.bind(this);
    }

    render() {
        console.log(this.props.unit)
        // If this Unit has a tenant, display it.  Otherwise, display "Vacant".
//        if (this.props.unit["tenants"].length > 0) {
//            var lease = this.props.unit["tenants"][0]["lease"];

            // If this tenant has a lease, display it.  Otherwise, display "month-to-month".
//            if (typeof(lease) != 'undefined' && lease != null) {
//                var leaseline = <p className="card-text">Rent: {lease["rent_amount"]}  {lease["start_date"]} to {lease["end_date"]}</p>;
//            } else {
//                var leaseline = <p className="card-text">Month-to-Month</p>;
//            } 
//        } else {
//            var tenant = <p className="card-text">Vacant: <a href="#">Add a Tenant</a></p>;
//        }

        // Create a uniqe ID for each card
        var uniqueid = `card-content-${this.state.unit["id"]}`;
        var tenantsid = `tenants-${this.state.unit["id"]}`;

        return (
            <div key={this.state.unit["id"]} className="card mb-3">
                {this.state.showcontent && 
                    <div className="row no-gutters" id={uniqueid}>
                        <div className="col-md-3">
                            <svg width="8em" height="8em" viewBox="0 0 16 16" className="bi bi-house-door" fill="rgb(1, 143, 1)" xmlns="http://www.w3.org/2000/svg">
                                <path fillRule="evenodd" d="M7.646 1.146a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 .146.354v7a.5.5 0 0 1-.5.5H9.5a.5.5 0 0 1-.5-.5v-4H7v4a.5.5 0 0 1-.5.5H2a.5.5 0 0 1-.5-.5v-7a.5.5 0 0 1 .146-.354l6-6zM2.5 7.707V14H6v-4a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 .5.5v4h3.5V7.707L8 2.207l-5.5 5.5z"/>
                                <path fillRule="evenodd" d="M13 2.5V6l-2-2V2.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5z"/>
                            </svg>
                        </div>
                        <div className="col-md-8">
                            <div className="card-body">
                                <h5 className="card-title">{this.state.unit["nickname"]}</h5>
                                <p className="card-text">{this.state.unit["address_line1"]}, {this.state.unit["address_line2"]} {this.state.unit["city"]}, {this.state.unit["state"]} {this.state.unit["zipcode"]}</p>
                                <div id={tenantsid}>
                                    <TenantList tenants={this.state.unit["tenants"]} unit={this.state.unit} />
                                </div>
                            </div>
                        </div>
                        <div className="col-md-1">
                            <div className="row no-gutters">
                                <button type="button" class="btn btn-primary" onClick={this.edit_click}>Edit</button>
                                
                            </div>
                        </div>
                    </div>
                }
                {this.state.showeditform && <EditUnitForm unit={this.state.unit} callback={this.EditUnitSubmit} delete={this.DeleteUnit} />}
                {this.state.newunit && <EditUnitForm unit={this.state.unit} callback={this.NewUnitSubmit} newunit={true} cancel={this.props.cancel} />}
            </div>
        );
    }

    edit_click() {

        console.log(this.state);
        
        // Hide Unit Content and show the edit form
        this.setState({
            showcontent: false,
            showeditform: true
        });
    }

    // https://medium.com/@ruthmpardee/passing-data-between-react-components-103ad82ebd17
    EditUnitSubmit = (childunit) => {

        // Retrieve the CSRF token from html
        const csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

        // PUT data from childunit to API
        fetch('/updateunit', {
            method: 'PUT',
            headers: {'X-CSRFToken': csrftoken},
            body: JSON.stringify({childunit})
            
        })
        .then(response => response.json())
        .then(result => {
            console.log(result);

            // Update state with unit data and show/hide flags
            this.setState({
                unit: childunit,
                showcontent: true,
                showeditform: false
            });
        });
    }

    NewUnitSubmit = (childunit) => {
        
        // Retrieve the CSRF token from html
        const csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

        // POST data from childunit to API
        fetch('/updateunit', {
            method: 'POST',
            headers: {'X-CSRFToken': csrftoken},
            body: JSON.stringify({childunit})
            
        })
        .then(response => response.json())
        .then(result => {
            console.log(result);
            
            // Add the id from JsonResponse to the childunit object
            childunit.id = result.id;

            // Update state with unit data and show/hide flags
            this.setState({
                unit: childunit,
                showcontent: true,
                newunit: false,
            });

            // Pass new unit back to UnitList
            this.props.callback(childunit);
        });        
    }

    DeleteUnit(childunit) {

        // Retrieve the CSRF token from html
        const csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

        // PUT request to API
        fetch('/deleteunit', {
            method: 'PUT',
            headers: {'X-CSRFToken': csrftoken},
            body: JSON.stringify({childunit})
            
        })
        .then(response => response.json())
        .then(result => {
            console.log(result);
        })

        // Delete unit from UnitList state via callback
        this.props.delete(childunit);
    }
}


class EditUnitForm extends React.Component {

    constructor(props) {
        super(props);
 
        this.state = {
            unit: this.props.unit,
        }
        this.handle_change = this.handle_change.bind(this);
        this.handle_submit = this.handle_submit.bind(this);
        this.delete_unit = this.delete_unit.bind(this);
    };

    handle_change(event) {
        const name = event.target.name;
        var value = event.target.value;

        // https://stackoverflow.com/questions/49348996/react-change-a-json-object-in-setstate
        this.setState(prevState => ({
            unit: {
                ...prevState.unit,
                [name]: value
            }
        }));
    }

    handle_submit() {
        this.props.callback(this.state.unit);
    }
    
    delete_unit() {
        this.props.delete(this.state.unit);
    }

    render() {
        return (
            <div className="row no-gutters">
                <div className="col-md-3" style={{backgroundColor: "grey"}}>
                    <svg width="8em" height="8em" viewBox="0 0 16 16" className="bi bi-house-door" fill="rgb(1, 143, 1)" xmlns="http://www.w3.org/2000/svg">
                        <path fillRule="evenodd" d="M7.646 1.146a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 .146.354v7a.5.5 0 0 1-.5.5H9.5a.5.5 0 0 1-.5-.5v-4H7v4a.5.5 0 0 1-.5.5H2a.5.5 0 0 1-.5-.5v-7a.5.5 0 0 1 .146-.354l6-6zM2.5 7.707V14H6v-4a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 .5.5v4h3.5V7.707L8 2.207l-5.5 5.5z"/>
                        <path fillRule="evenodd" d="M13 2.5V6l-2-2V2.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5z"/>
                    </svg>
                </div>
                <div className="col-md-9">
                    <div className="form-group">
                        <div className="input-group input-group-sm mb-3">
                            <div className="input-group-prepend">
                                <span className="input-group-text" id="inputGroup-sizing-sm">Nickname</span>
                            </div>
                            <input name="nickname" type="text" value={this.state.unit["nickname"]} onChange={this.handle_change.bind(this)} className="form-control" aria-label="Nickname" aria-describedby="inputGroup-sizing-sm"></input>
                        </div>
                        <div className="input-group input-group-sm mb-3">
                            <div className="input-group-prepend">
                                <span className="input-group-text" id="inputGroup-sizing-sm">Street Address Line 1</span>
                            </div>
                            <input name="address_line1" type="text" value={this.state.unit["address_line1"]} onChange={this.handle_change} className="form-control" aria-label="Street Address Line 1" aria-describedby="inputGroup-sizing-sm"></input>
                        </div>
                        <div className="input-group input-group-sm mb-3">
                            <div className="input-group-prepend">
                                <span className="input-group-text" id="inputGroup-sizing-sm">Street Address Line 2</span>
                            </div>
                            <input name="address_line2" type="text" value={this.state.unit["address_line2"]} onChange={this.handle_change} className="form-control" aria-label="Street Address Line 2" aria-describedby="inputGroup-sizing-sm"></input>
                        </div>
                        <div className="input-group input-group-sm mb-3">
                            <div className="input-group-prepend">
                                <span className="input-group-text" id="inputGroup-sizing-sm">City</span>
                            </div>
                            <input name="city" type="text" value={this.state.unit["city"]} onChange={this.handle_change} className="form-control" aria-label="City" aria-describedby="inputGroup-sizing-sm"></input>
                        </div>
                        <div className="input-group input-group-sm mb-3">
                            <div className="input-group-prepend">
                                <span className="input-group-text" id="inputGroup-sizing-sm">State</span>
                            </div>
                            <select name="state" value={this.state.unit["state"]} onChange={this.handle_change} class="form-control" aria-label="Street Address Line 1" aria-describedby="inputGroup-sizing-sm">
                                <option value="AL">Alabama</option>
                                <option value="AK">Alaska</option>
                                <option value="AZ">Arizona</option>
                                <option value="AR">Arkansas</option>
                                <option value="CA">California</option>
                                <option value="CO">Colorado</option>
                                <option value="CT">Connecticut</option>
                                <option value="DE">Delaware</option>
                                <option value="DC">District Of Columbia</option>
                                <option value="FL">Florida</option>
                                <option value="GA">Georgia</option>
                                <option value="HI">Hawaii</option>
                                <option value="ID">Idaho</option>
                                <option value="IL">Illinois</option>
                                <option value="IN">Indiana</option>
                                <option value="IA">Iowa</option>
                                <option value="KS">Kansas</option>
                                <option value="KY">Kentucky</option>
                                <option value="LA">Louisiana</option>
                                <option value="ME">Maine</option>
                                <option value="MD">Maryland</option>
                                <option value="MA">Massachusetts</option>
                                <option value="MI">Michigan</option>
                                <option value="MN">Minnesota</option>
                                <option value="MS">Mississippi</option>
                                <option value="MO">Missouri</option>
                                <option value="MT">Montana</option>
                                <option value="NE">Nebraska</option>
                                <option value="NV">Nevada</option>
                                <option value="NH">New Hampshire</option>
                                <option value="NJ">New Jersey</option>
                                <option value="NM">New Mexico</option>
                                <option value="NY">New York</option>
                                <option value="NC">North Carolina</option>
                                <option value="ND">North Dakota</option>
                                <option value="OH">Ohio</option>
                                <option value="OK">Oklahoma</option>
                                <option value="OR">Oregon</option>
                                <option value="PA">Pennsylvania</option>
                                <option value="RI">Rhode Island</option>
                                <option value="SC">South Carolina</option>
                                <option value="SD">South Dakota</option>
                                <option value="TN">Tennessee</option>
                                <option value="TX">Texas</option>
                                <option value="UT">Utah</option>
                                <option value="VT">Vermont</option>
                                <option value="VA">Virginia</option>
                                <option value="WA">Washington</option>
                                <option value="WV">West Virginia</option>
                                <option value="WI">Wisconsin</option>
                                <option value="WY">Wyoming</option>
                            </select>
                        </div>
                        <div className="input-group input-group-sm mb-3">
                            <div className="input-group-prepend">
                                <span className="input-group-text" id="inputGroup-sizing-sm">Zip Code</span>
                            </div>
                            <input name="zipcode" type="text" value={this.state.unit["zipcode"]} onChange={this.handle_change} className="form-control" aria-label="Zip Code" aria-describedby="inputGroup-sizing-sm"></input>
                        </div>
                        <button type="button" class="btn btn-primary" onClick={this.handle_submit}>Save</button>
                        {this.props.newunit ?
                            <button type="button" class="btn btn-danger" onClick={this.props.cancel}>Cancel</button>
                            :
                            <button type="button" class="btn btn-danger" onClick={this.delete_unit}>Delete Unit</button>
                        }
                    </div>
                </div>
            </div>
        );
    }   
};

class TenantList extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            tenants: this.props.tenants,
            newtenant: false,
            vacant: this.props.vacant
        }
        this.new_tenant = this.new_tenant.bind(this);
        this.add_tenant = this.add_tenant.bind(this);
        this.delete_tenant = this.delete_tenant.bind(this);
    }

    render() {

        const tenants = this.state.tenants

        if (typeof tenants !== 'undefined' && tenants.length > 0) {
            return (
                <div className="tenants">
                        <ul>
                            {tenants.map(tenant =>
                                <Tenant tenant={tenant} showcontent={true} showeditform={false} newtenant={false} unit={this.props.unit} delete={this.delete_tenant} />
                            )}
                            {this.state.newtenant && <Tenant tenant={{"tenant_first": ""}} newtenant={true} callback={this.add_tenant} unit={this.props.unit} cancel={this.cancel_tenant} />}
                        </ul>
                    {this.state.newtenant ? '' : <button onClick={this.new_tenant} type="button" class="btn btn-outline-primary" id="add-tenant">Add Tenant +</button>}
                </div>
            );
        }
        return (
            <div className="tenants">
                <p className="card-text">Vacant: <a href="#" onClick={this.new_tenant}>Add a Tenant</a></p>
                {this.state.newtenant && <Tenant tenant={{"tenant_first": ""}} newtenant={true} callback={this.add_tenant} unit={this.props.unit} cancel={this.cancel_tenant} />}
            </div>
        );
    }

    new_tenant() {
        this.setState({
            newtenant: true
        });
    }

    add_tenant(childtenant) {
        this.setState({
            tenants: this.state.tenants.concat(childtenant),
            newtenant: false
        });
    }

    delete_tenant = (childtenant) => {

        // Filter the deleted tenant out of the state
        const newtenantslist = this.state.tenants.filter((tenant) => {
            return tenant.id !== childtenant.id
        });

        // Set the vacant prop based on whether or not there are tenants in the list.
        if (newtenantslist.length > 0) {
            var vac = false;
        } else {
            var vac = true;
        }

        // Re-render the TenantList component
        const tenantsdiv = document.querySelector(`#tenants-${this.props.unit.id}`);
        ReactDOM.render(<TenantList tenants={newtenantslist} vacant={vac} unit={this.props.unit} delete={this.props.delete} />, tenantsdiv);
    }

    cancel_tenant = () => {
        
        // Set newtenant flag back to false
        this.setState({
            newunit: false
        });

        // Re-render the TenantList component
        const tenantsdiv = document.querySelector(`#tenants-${this.props.unit.id}`);
        ReactDOM.render(<TenantList tenants={this.props.tenants} vacant={this.props.vacant} unit={this.props.unit} />, tenantsdiv);
    }

}


class Tenant extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            tenant: this.props.tenant,
            showcontent: this.props.showcontent,
            showeditform: this.props.showeditform,
            newtenant: this.props.newtenant
        }
        this.NewTenantSubmit = this.NewTenantSubmit.bind(this);
        this.edit_click = this.edit_click.bind(this);
        this.DeleteTenant = this.DeleteTenant.bind(this);
    }

    render() {
        return [
            <div>
                {this.state.showcontent &&
                    <div className="row no-gutters">
                        <p className="card-text">Tenant: {this.state.tenant["tenant_first"]} {this.state.tenant["tenant_last"]} -- Email: {this.state.tenant["tenant_email"]}</p>
                        <a className="edit-tenant" href="#" onClick={this.edit_click}>Edit</a>

                    </div>
                }
                {this.state.showeditform && <EditTenantForm tenant={this.state.tenant} callback={this.EditTenantSubmit} newtenant={false} delete={this.DeleteTenant}/>}
                {this.state.newtenant && <EditTenantForm tenant={this.state.tenant} callback={this.NewTenantSubmit} newtenant={true} cancel={this.props.cancel} />}
            </div>
            
        ]
    }

    edit_click() {

        console.log(this.state);
        
        // Hide Unit Content and show the edit form
        this.setState({
            showcontent: false,
            showeditform: true
        });
    }

    NewTenantSubmit(childtenant) {
        
        // Retrieve the CSRF token from html
        const csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        
        // Set the New tenant's unit ID to the current unit's ID
        childtenant.unit_id = this.props.unit.id

        // POST data from childtenant to API
        fetch('/updatetenant', {
            method: 'POST',
            headers: {'X-CSRFToken': csrftoken},
            body: JSON.stringify({childtenant})
            
        })
        .then(response => response.json())
        .then(result => {
            console.log(result);
            
             // Add the id from JsonResponse to the childunit object
             childtenant.id = result.id;

            // Update state with tenant data and show/hide flags
            this.setState({
                tenant: childtenant,
                showcontent: true,
                newtenant: false,
            });

            // Pass new tenant back to TenantList
            this.props.callback(childtenant);
        });
    }

    // https://medium.com/@ruthmpardee/passing-data-between-react-components-103ad82ebd17
    EditTenantSubmit = (childtenant) => {

        // Retrieve the CSRF token from html
        const csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

        // Set the New tenant's unit ID to the current unit's ID
        childtenant.unit_id = this.props.unit.id

        // PUT data from childtenant to API
        fetch('/updatetenant', {
            method: 'PUT',
            headers: {'X-CSRFToken': csrftoken},
            body: JSON.stringify({childtenant})
            
        })
        .then(response => response.json())
        .then(result => {
            console.log(result);
        });
        // Update state with tenant data and show/hide flags
        this.setState({
            tenant: childtenant,
            showcontent: true,
            showeditform: false
        });
    }

    DeleteTenant(childtenant) {

        // Retrieve the CSRF token from html
        const csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

        // Set the New tenant's unit ID to the current unit's ID
        childtenant.unit_id = this.props.unit.id

        // PUT request to API
        fetch('/deletetenant', {
            method: 'PUT',
            headers: {'X-CSRFToken': csrftoken},
            body: JSON.stringify({childtenant})
            
        })
        .then(response => response.json())
        .then(result => {
            console.log(result);
        })

        // Delete tenant from TenantList state via callback
        this.props.delete(childtenant);
    }
}


class EditTenantForm extends React.Component {

    constructor(props) {
        super(props);
 
        this.state = {
            tenant: this.props.tenant,
        }
        this.handle_change = this.handle_change.bind(this);
        this.handle_submit = this.handle_submit.bind(this);
        this.delete_tenant = this.delete_tenant.bind(this);
    };

    handle_change(event) {
        const name = event.target.name;
        var value = event.target.value;

        // https://stackoverflow.com/questions/49348996/react-change-a-json-object-in-setstate
        this.setState(prevState => ({
            tenant: {
                ...prevState.tenant,
                [name]: value
            }
        }));
    }

    handle_submit() {
        this.props.callback(this.state.tenant);
    }

    delete_tenant() {
        this.props.delete(this.state.tenant);
    }

    render() {
        return(
            <div class="form-row">
                <div className="input-group input-group-sm mb-3">
                    <div className="input-group-prepend">
                        <span className="input-group-text" id="inputGroup-sizing-sm">First</span>
                    </div>
                    <input name="tenant_first" type="text" value={this.state.tenant["tenant_first"]} onChange={this.handle_change.bind(this)} className="form-control" aria-label="tenant_first" aria-describedby="inputGroup-sizing-sm"></input>
                </div>
                <div className="input-group input-group-sm mb-3">
                    <div className="input-group-prepend">
                        <span className="input-group-text" id="inputGroup-sizing-sm">Last</span>
                    </div>
                    <input name="tenant_last" type="text" value={this.state.tenant["tenant_last"]} onChange={this.handle_change.bind(this)} className="form-control" aria-label="tenant_last" aria-describedby="inputGroup-sizing-sm"></input>
                </div>
                <div className="input-group input-group-sm mb-3">
                    <div className="input-group-prepend">
                        <span className="input-group-text" id="inputGroup-sizing-sm">Email</span>
                    </div>
                    <input name="tenant_email" type="text" value={this.state.tenant["tenant_email"]} onChange={this.handle_change.bind(this)} className="form-control" aria-label="tenant_email" aria-describedby="inputGroup-sizing-sm"></input>
                </div>
                <button type="button" class="btn btn-primary" onClick={this.handle_submit}>Save</button>
                {this.props.newtenant ?
                    <button type="button" class="btn btn-danger" onClick={this.props.cancel}>Cancel</button>
                    :
                    <button type="button" class="btn btn-danger" onClick={this.delete_tenant}>Delete Tenant</button>
                }
            </div>
        );
    }
}


class UnitList extends React.Component {
    
    constructor(props) {
        super(props);
 
        this.state = {
            units: [],
            newunit: false
        }
        this.add_unit = this.add_unit.bind(this);
        this.new_unit = this.new_unit.bind(this);
    }

    // https://www.robinwieruch.de/react-fetching-data 
    componentDidMount() {
        fetch("/getunits")
            .then(response => response.json())
            .then(data => this.setState({ units: data }));
    }
 
    render() {
        const { units } = this.state;
     
        return [
            <div>
                <ul>
                    {units.map(unit =>
                        <Unit unit={unit} showcontent={true} showeditform={false} newunit={false} delete={this.delete_unit} />
                    )}
                    {this.state.newunit && <Unit unit={{"tenants": ""}} showcontent={false} showeditform={false} newunit={true} callback={this.add_unit} delete={this.delete_unit} cancel={this.cancel_unit} />}
                </ul>
                {this.state.newunit ? '' : <button onClick={this.new_unit} type="button" class="btn btn-outline-primary" id="add-unit">Add Unit +</button>}
            </div>
        ];
    }

    new_unit() {
        this.setState({
            newunit: true
        });
    }

    add_unit(childunit) {

        // Append the childunit to state units and reset the newunit flag to false.
        this.setState({
            units: this.state.units.concat(childunit),
            newunit: false
        });
    }

    delete_unit = (childunit) => {

        // Filter the deleted unit out of the state
        const newunitslist = this.state.units.filter((unit) => {
            return unit.id !== childunit.id
        });

        console.log(newunitslist)

        // Set state to the new unit list
        this.setState({
            units: newunitslist
        });

        // Re-render the UnitList component
        ReactDOM.render(<UnitList />, div);
    }

    cancel_unit = () => {
        
        // Set newunit flag back to false
        this.setState({
            newunit: false
        });

        // Re-render the UnitList component
        ReactDOM.render(<UnitList />, div);
    }

}



const div = document.querySelector('#unit-list');
ReactDOM.render(React.createElement(UnitList), div);