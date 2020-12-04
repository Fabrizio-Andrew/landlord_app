class Unit extends React.Component {

    constructor(props) {
        super(props);
 
        this.state = {
            unit: null,
        };
    }

    render() {

        // If this Unit has a tenant, display it.  Otherwise, display "Vacant".
        if (this.props.unit["tenants"].length > 0) {
            var tenant = <p className="card-text">Tenant: {this.props.unit["tenants"][0]["tenant_first"]} {this.props.unit["tenants"][0]["tenant_last"]}</p>;
            var remtenant = <div className="row no-gutters"><button type="button" class="btn btn-primary">Remove Tenant</button></div>;
            var lease = this.props.unit["tenants"][0]["lease"];

            // If this tenant has a lease, display it.  Otherwise, display "month-to-month".
            if (typeof(lease) != 'undefined' && lease != null) {
                var leaseline = <p className="card-text">Rent: {lease["rent_amount"]}  {lease["start_date"]} to {lease["end_date"]}</p>;
            } else {
                var leaseline = <p className="card-text">Month-to-Month</p>;
            }
        } else {
            var tenant = <p className="card-text">Vacant: <a href="#">Add a Tenant</a></p>;
        }

        // Create a uniqe ID for each card
        var uniqueid = `card-number-${this.props.unit["id"]}`;

        return (
            <div key={this.props.unit["id"]} className="card mb-3" id={uniqueid}>
                <div className="row no-gutters">
                    <div className="col-md-3" style={{backgroundColor: "grey"}}>
                        <svg width="8em" height="8em" viewBox="0 0 16 16" className="bi bi-house-door" fill="rgb(1, 143, 1)" xmlns="http://www.w3.org/2000/svg">
                            <path fillRule="evenodd" d="M7.646 1.146a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 .146.354v7a.5.5 0 0 1-.5.5H9.5a.5.5 0 0 1-.5-.5v-4H7v4a.5.5 0 0 1-.5.5H2a.5.5 0 0 1-.5-.5v-7a.5.5 0 0 1 .146-.354l6-6zM2.5 7.707V14H6v-4a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 .5.5v4h3.5V7.707L8 2.207l-5.5 5.5z"/>
                            <path fillRule="evenodd" d="M13 2.5V6l-2-2V2.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5z"/>
                        </svg>
                    </div>
                    <div className="col-md-7">
                        <div className="card-body">
                            <h5 className="card-title">{this.props.unit["nickname"]}</h5>
                            <p className="card-text">{this.props.unit["address_line1"]}, {this.props.unit["address_line2"]} {this.props.unit["city"]}, {this.props.unit["state"]} {this.props.unit["zipcode"]}</p>
                            {tenant}
                            {leaseline}
                        </div>
                    </div>
                    <div className="col-md-2" style={{backgroundColor: "grey"}}>
                        <div className="row no-gutters">
                            <button onClick ={this.edit_unit} type="button" class="btn btn-primary">Edit</button>
                        </div>
                        {remtenant}
                    </div>
                </div>
            </div>
        );
    }

    edit_unit() {

        console.log(this.state.unit["id"]);
        // Get the current Unit Card
        var unitcard = document.querySelector(`#card-number-${this.state.unit["id"]}`);
    
        // Clear the Unit Card
        unitcard.style.display = 'none';
    
        // Display the Edit Unit Form
        ReactDOM.render(React.createElement(<EditUnitForm unit={this.state.unit}/>), unitcard);
    }
}



class EditUnitForm extends React.Component {

    constructor(props) {
        super(props);
 
        this.state = {
            unit: null,
        };
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
                            <input type="text" className="form-control" aria-label="Nickname" aria-describedby="inputGroup-sizing-sm">{this.props.unit["nickname"]}</input>
                        </div>
                        <div className="input-group input-group-sm mb-3">
                            <div className="input-group-prepend">
                                <span className="input-group-text" id="inputGroup-sizing-sm">Street Address Line 1</span>
                            </div>
                            <input type="text" className="form-control" aria-label="Street Address Line 1" aria-describedby="inputGroup-sizing-sm">{this.props.unit["address_line1"]}</input>
                        </div>
                        <div className="input-group input-group-sm mb-3">
                            <div className="input-group-prepend">
                                <span className="input-group-text" id="inputGroup-sizing-sm">Street Address Line 2</span>
                            </div>
                            <input type="text" className="form-control" aria-label="Street Address Line 2" aria-describedby="inputGroup-sizing-sm"></input>
                        </div>
                        <div className="input-group input-group-sm mb-3">
                            <div className="input-group-prepend">
                                <span className="input-group-text" id="inputGroup-sizing-sm">City</span>
                            </div>
                            <input type="text" className="form-control" aria-label="City" aria-describedby="inputGroup-sizing-sm"></input>
                        </div>
                        <div className="input-group input-group-sm mb-3">
                            <div className="input-group-prepend">
                                <span className="input-group-text" id="inputGroup-sizing-sm">State</span>
                            </div>
                            <select class="form-control" aria-label="Street Address Line 1" aria-describedby="inputGroup-sizing-sm">
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
                            <input type="text" className="form-control" aria-label="Zip Code" aria-describedby="inputGroup-sizing-sm"></input>
                        </div>
                        

                        
                    </div>
                </div>
            </div>
        );
    }
    
}

class AddUnitButton extends React.Component {

    render() {
        return (<button onClick={this.show_form} type="button" class="btn btn-outline-primary" id="add-unit">Add Unit +</button>);
    }

    show_form() {

        // Hide the Add Unit Button
        document.querySelector('#add-unit').style.display = 'none';

        // Add a new div to hold our Add Unit Form
        var formdiv = document.createElement('div');
        div.append(formdiv);

        // Display the Add Unit Form Component
        ReactDOM.render(React.createElement(AddUnitForm), formdiv);
    }
}

class AddUnitForm extends React.Component {
    
    // Actually... this should probably be broken out into it's own html page...
    render() {

        return(<p>Put a form here!</p>);
    }
}

class UnitList extends React.Component {
    
    constructor(props) {
        super(props);
 
        this.state = {
            units: [],
        };
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
            <ul>
                {units.map(unit =>
                    <Unit unit={unit} />
                )}
            </ul>,
            <AddUnitButton />
        ];
    }
}

const div = document.querySelector('#unit-list');
ReactDOM.render(React.createElement(UnitList), div);