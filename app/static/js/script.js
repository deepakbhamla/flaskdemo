function fileValue(value) {
    var path = value.value;
    var extenstion = path.split('.').pop();
    if(extenstion == "pdf" || extenstion == "txt"){
        document.getElementById('image-preview').src = window.URL.createObjectURL(value.files[0]);
        var filename = path.replace(/^.*[\\\/]/, '').split('.').slice(0, -1).join('.');
        document.getElementById("filename").innerHTML = filename;
    }else{
        alert("File not supported kindly ipload pdf")
    }
}