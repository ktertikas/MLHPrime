
chrome.runtime.onInstalled.addListener(function() {
 
    //console.log("Tag Your Stuff is saving your bookmarks! FUCK MARIOS!!!!");
 
    var bm_urls = new Array();

    function fetch_bookmarks(parentNode){
        parentNode.forEach(function(bookmark) {
            if(! (bookmark.url === undefined || bookmark.url === null)) {
                bm_urls.push(bookmark.url);
            }
            if (bookmark.children) {
                fetch_bookmarks(bookmark.children);
            }
        });
    }

    //Show bootbox dialog
    /*bootbox.confirm({
        message: "This is a confirm with custom button text and color! Do you like it?",
        buttons: {
            confirm: {
                label: 'Yes',
                className: 'btn-success'
            },
            cancel: {
                label: 'No',
                className: 'btn-danger'
            }
        },
        callback: function (result) {
            console.log('This was logged in the callback: ' + result);
        }
    });*/

    var retVal = confirm("Tag Your Stuff would like to add your bookmarks to its clustering platform. Would you like to continue?");
    if( retVal == true ){
      //Send to platform
      chrome.bookmarks.getTree(function(rootNode) {
            fetch_bookmarks(rootNode);
            console.log(JSON.stringify(bm_urls));
        });
      return true;
    }
    else{
      //document.write ("User does not want to continue!");
      return false;
    }
});