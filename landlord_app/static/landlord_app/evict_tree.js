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
    button.onclick = () => {
        pass
    }

    div.append(question, note, dropdown, button);

    document.querySelector('#evict-tree').append(div);

}