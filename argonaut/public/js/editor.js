// Javascript functionality for post editor form, The Argonaut
// Author: Jason Robinson, Basshero.org, 2010

function toggleTag(existing_tags,name) {
    // Function to toggle tag in editor tags field
    var tags = existing_tags.split(';');
    var found = false;
    var newArray = new Array();
    name = name.toLowerCase().trim()
    if (tags.length > 0) {
        for (var i in tags) {
            if (tags[i].length > 0) {
                if (tags[i] == name) {
                    // skip, ie remove
                    found = true;
                } else {
                    // keep
                    newArray.push(tags[i]);
                }
            }
        }
    }
    if (! found) {
        // add if not found
        newArray.push(name);
    }
    // update form
    document.getElementById('tags').value = newArray.join(";");
    // toggle css property
    toggleTagCSS(name)
    return false;
}

function toggleTagCSS(tag) {
    // Toggle the CSS effect of a tag
    if (document.getElementById('tag_'+tag).style.backgroundColor) {
        document.getElementById('tag_'+tag).style.backgroundColor = null;
    } else {
        document.getElementById('tag_'+tag).style.backgroundColor = '#BBD9EE';
    }
}

function toggleAllTags(existing_tags) {
    // Toggle all current tags
    var tags = existing_tags.split(';');
    for (var i in tags) {
        if (tags[i].length > 0) {
            toggleTagCSS(tags[i])
        }
    }
}
