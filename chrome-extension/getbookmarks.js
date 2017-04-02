
chrome.runtime.onInstalled.addListener(function() {
 
    console.log("Tag Your Stuff is saving your bookmarks! FUCK MARIOS!!!!");
 
    var bm_urls = new Array();
 
    function fetch_bookmarks(parentNode) {
        var retVal = confirm("Tag Your Stuff would like to add your bookmarks to its clustering platform. Would you like to continue?");
       if( retVal == true ){
          parentNode.forEach(function(bookmark) {
                if(! (bookmark.url === undefined || bookmark.url === null)) {
                    bm_urls.push(bookmark.url);
                }
                if (bookmark.children) {
                    fetch_bookmarks(bookmark.children);
                }
            });
          return true;
       }
       else{
          //document.write ("User does not want to continue!");
          return false;
       }
    }
 
    chrome.bookmarks.getTree(function(rootNode) {
        fetch_bookmarks(rootNode);
        console.log(JSON.stringify(bm_urls));
    });
});