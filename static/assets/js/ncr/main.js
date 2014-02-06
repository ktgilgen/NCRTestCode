$().ready(function() {
          refreshUsers();
          //registerForm();
          }

function getmodels(callback) {
    // Get the current models via AJAX
    $.ajax({ url: '/get_models', }).done(function (response) {
                                         var models = JSON.parse(response);
                                         // since this call is asynchronous, we need to pass the
                                         
                                         callback(models);
                                         });
}

          function refreshUsers() {
          getUsers(function(users) {
                   var name, html, button;
                   // This removes the previous list of users
                   $('#userList').html('');
                   // This is an underscore function. Instead of using a for loop,
                   // we can use the each function to iterate over the list. It makes
                   // The code look cleaner and can help prevent errors related to array indices, etc.
                   _.each(users, function(user) {
                          // Create the text that will be displayed
                          name = user.username + ':' + user.firstName + ', ' + user.lastName;
                          // create the delete button with a data-ref attribute set to the username
                          button = '<button data-ref="' + user.username + '">Delete</button>';
                          // finally wrap it in a 'list item' tag (its going in an ordered list)
                          html = '<li>' + name + button + '</li>';
                          // Put it inside the list element
                          $('#userList').append(html);
                          
                          });
                   // Now lets register these new delete buttons so they work (the old
                   // ones are now invalid, since they don't exist!)
                   registerDeleteButtons();
                   });
          }