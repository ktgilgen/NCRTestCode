
$().ready(function () {
    // Load the existing users from Mongo
    alert("ENTERED READY.");
    refreshDB();
});

function getDB(callback) {
    // Get the current models via AJAX
    $.ajax({ url: '/get_db', }).done(function (response) {
        var db = JSON.parse(response);
        alert("This is the response from server.py: " + response);
        // since this call is asynchronous, we need to pass the
        // value to a callback function that is run when the
        // AJAX call is done
        callback(db);
    });
}

function refreshDB() {
    alert("ENTERED REFRESH");
    getDB(function (models) {
        var name, html, button;
        // This removes the previous list of models
        $('#modelList').html('');
        _.each(models, function (model) {
            // Create the text that will be displayed in the model list
            name = model.model_name + ':x,y,z,v,i,b';
            $('#modelList').append(html);

        });
    });
}