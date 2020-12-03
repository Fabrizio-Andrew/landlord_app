document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#continue').onclick = () => tree_start();
});

function tree_start() {

    // Clear the evict-tree div
    document.querySelector('#evict-tree').innerHTML = '';

    // Present first question
    const div = document.createElement('div');
    div.className = 'form';

    const question = document.createElement('h2');
    question.innerHTML = 'What state is your rental property located in?';

    const note = document.createElement('p');
    note.innerHTML = 'NOTE: Maryland is the only state currently supported.'

    const dropdown = document.createElement('select');
    dropdown.className = 'form-control';
    dropdown.add(new Option('Maryland', 'MD'));

    const button = document.createElement('button');
    button.className = 'btn btn-lg btn-primary btn-block';
    button.innerHTML = 'Continue';
    button.onclick = function(dropdown.value) {
        
        // Set state as global var
        state = dropdown.value;

        // Clear the evict-tree div
        document.querySelector('#evict-tree').innerHTML = '';

        // Get rental rules for this state
        fetch(`/rules/${state}`)
        .then(response => response.json())
        .then(respjson => {

            // set rules to global variable
            staterules = respjson;

            if (staterules.mtom === True) {

                const question = document.createElement('h2');
                question.innerHTML = 'Do you have a current lease agreement with the tenant at this property?';

                const yesbutton = document.createElement('button');
                yesbutton.className = 'btn btn-lg btn-primary btn-block';
                yesbutton.innerHTML = 'Yes';
                yesbutton.onclick = () => {
                    pass
                }

                const nobutton = document.createElement('button');
                nobutton.className = 'btn btn-lg btn-primary btn-block';
                nobutton.innerHTML = 'No';
                nobutton.onclick = () => {
                    
                    // Clear the evict-tree div
                    document.querySelector('#evict-tree').innerHTML = '';

                    const question = document.createElement('h2');
                    question.innerHTML = 'Have you provided the tenant with a written 30-day Notice to Vacate and allowed the full 30 days to expire?'
                    
                    const yesbutton = document.createElement('button');
                    yesbutton.className = 'btn btn-lg btn-primary btn-block';
                    yesbutton.innerHTML = 'Yes';

                    const nobutton = document.createElement('button');
                    nobutton.className = 'btn btn-lg btn-primary btn-block';
                    nobutton.innerHTML = 'No';



                }

                document.querySelector('#evict-tree').append(question, yesbutton, nobutton);
            }
        });




    }

    div.append(question, note, dropdown, button);

    document.querySelector('#evict-tree').append(div);

};