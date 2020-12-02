class Unit extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            unit: null
        };
    }

    render() {
        return (
            <div className="card mb-3">
                <div className="row no-gutters">
                    <div className="col-md-3">
                        <svg width="8em" height="8em" viewBox="0 0 16 16" className="bi bi-house-door" fill="green" xmlns="http://www.w3.org/2000/svg">
                            <path fillRule="evenodd" d="M7.646 1.146a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 .146.354v7a.5.5 0 0 1-.5.5H9.5a.5.5 0 0 1-.5-.5v-4H7v4a.5.5 0 0 1-.5.5H2a.5.5 0 0 1-.5-.5v-7a.5.5 0 0 1 .146-.354l6-6zM2.5 7.707V14H6v-4a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 .5.5v4h3.5V7.707L8 2.207l-5.5 5.5z"/>
                            <path fillRule="evenodd" d="M13 2.5V6l-2-2V2.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5z"/>
                        </svg>
                    </div>
                    <div className="col-md-8">
                        <div className="card-body">
                            <h5 className="card-title">{this.props.unit["nickname"]}</h5>
                            <p className="card-text">{this.props.unit["address_line1"]}, {this.props.unit["address_line2"]}</p>
                            <p className="card-text">{this.props.unit["city"]}, {this.props.unit["state"]} {this.props.unit["zipcode"]}</p>
                            <p className="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                            <p className="card-text"><small className="text-muted">Last updated 3 mins ago</small></p>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

class UnitList extends React.Component {
    
    constructor(props) {
        super(props);
        this.state = {
            list: null
        };
    }
    
    render() {
        return (
            <div> 
                {result.map((unit) => <Unit unit={unit} />)}
            </div>
        );
    }
};


fetch('/getunits')
.then(response => response.json())
.then(result => {
    console.log(result);
    return <UnitList list={result} />
});
    
//        console.log(unit);



//    ReactDOM.render(<Unit unit={unit} />, document.querySelector("#unit_list"));
//})