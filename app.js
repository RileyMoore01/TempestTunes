const clientId = 'ad34ee7e945b48349f261a4cf6d9006d';
const clientSecret = '71eae9aaed0d4840ab0509c5fcfc29af';
const redirectURI = 'http://127.0.0.1:5500/index.html';

var access_token = null;
var refresh_token = null;

const AUTHORIZE = 'https://accounts.spotify.com/authorize'
const TOKEN = 'https://accounts.spotify.com/api/token'
const PLAYLISTS = "https://api.spotify.com/v1/me/playlists";
const USER = "https://api.spotify.com/v1/me"
const HWINTER = "https://api.spotify.com/v1/playlists/0KQoD1gO2X9KwDP8tG4mR2"
const AWINTER = "https://api.spotify.com/v1/playlists/6M0Y3K1g812tEorwbmbrsk"
const SWINTER = "https://api.spotify.com/v1/playlists/6aIRCjyVgqumnBjII6eqfv"
const ARAIN = "https://api.spotify.com/v1/playlists/1zYOGPjZuax1sv97pAn1QR"
const SRAIN = "https://api.spotify.com/v1/playlists/6VX42WTrkQfdezdGypHpXM"
const HRAIN = "https://api.spotify.com/v1/playlists/2SwKiduWvuNF5BdvP6KriI"
const AHOT = "https://api.spotify.com/v1/playlists/18YP1KE5D7vILbJYuftXt2"
const SHOT = "https://api.spotify.com/v1/playlists/4RvDPhoeOlp5ttiZ2qSiLk"
const HHOT = "https://api.spotify.com/v1/playlists/4Ffy3yTfU1xTCtleaR07wI"
const AWINDY = "https://api.spotify.com/v1/playlists/1SFWJg7yWTvopBM4XW8owt"
const SWINDY = "https://api.spotify.com/v1/playlists/7lG6NP07Vx3LqnYz3hEjSH"
const HWINDY = "https://api.spotify.com/v1/playlists/2quk8WZfpM7j8vqvWtO9xP"

function onPageLoad(){
    
    if(window.location.href.indexOf('code') > -1){
        let container = document.getElementById('container');
        let inputPageContainer = document.getElementById('inputPageContainer');
        inputPageContainer.style.display = 'grid'
        container.style.display = 'none'

        handleRedirect();
        
    }
    callApi("GET",USER,null,handleCurrentUserResponse)
    
}

window.onload = onPageLoad;

function handleRedirect(){
    let code = getCode();
    fetchAccessToken(code);
    window.history.pushState("","",redirectURI);
}

function getCode(){
    let code = null;
    const queryString = window.location.search;
    if(queryString.length > 0){
        const urlParams = new URLSearchParams(queryString);
        code = urlParams.get('code');
    }
    
    return code;
}

function fetchAccessToken( code ){
    let body = "grant_type=authorization_code";
    body += "&code=" + code; 
    body += "&redirect_uri=" + encodeURI(redirectURI);
    body += "&client_id=" + clientId;
    body += "&client_secret=" + clientSecret;
    
    callAuthorizationAPI(body);
    
}

function callAuthorizationAPI(body) {
    let xhr = new XMLHttpRequest();
    xhr.open("POST", TOKEN, true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.setRequestHeader('Authorization', 'Basic ' + btoa(clientId + ":" + clientSecret));
    xhr.send(body);
    xhr.onload = handleAuthorizationResponse;
}

function handleAuthorizationResponse(){
    if(this.status == 200){
    var data = JSON.parse(this.responseText);
        
        var data = JSON.parse(this.responseText);
        if ( data.access_token != undefined ){
            access_token = data.access_token;
            
            localStorage.setItem("access_token", access_token);
        }
        if ( data.refresh_token  != undefined ){
            refresh_token = data.refresh_token;
            localStorage.setItem("refresh_token", refresh_token);
        }
        console.log(this.responseText)
        onPageLoad();
    } else{
        console.log(this.responseText)
        alert(this.responseText)
    }
}

function requestAuth(){
    localStorage.setItem("client_id",clientId)
    localStorage.setItem("client_secret",clientSecret)

    let url = AUTHORIZE;
    url += "?client_id=" + clientId;
    url += "&response_type=code";
    url += "&redirect_uri=" + encodeURI(redirectURI);
    url += "&show_dialog=true";
    url += "&scope=playlist-modify-private ugc-image-upload user-read-private user-read-email user-modify-playback-state user-read-playback-position user-library-read streaming user-read-playback-state user-read-recently-played playlist-read-private";
    window.location.href = url; // Show Spotify's authorization screen
}

function callApi(method, url, body, callback){
    let xhr = new XMLHttpRequest();
    
    xhr.open(method, url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('Authorization', 'Bearer ' + access_token);
    xhr.send(body);
    xhr.onload = callback;
}

function handlePlaylistResponse(){
    if ( this.status == 200 ){
        var data = JSON.parse(this.responseText);
        console.log(data)
        data.items.forEach(item => addPlaylist(item));
    }
    else if ( this.status == 401 ){
        refreshAccessToken()
    }
    else {
        console.log(this.responseText);
        alert(this.responseText);
    }
}

function addPlaylist(item){
    let playlistContainer = document.createElement('div');
    let playlist = document.createElement("div");
    let cover = document.createElement('img');

    playlistContainer.className = 'playlistContainer'

    cover = createCover(cover, item);
    playlist = createPlaylist(playlist, item);

    playlistContainer.appendChild(cover);
    playlistContainer.appendChild(playlist);

    document.getElementById('playlistWrapper').appendChild(playlistContainer);
}

function createPlaylist(playlist, item) {
    let TRACKS = `https://api.spotify.com/v1/playlists/${item.id}/tracks?limit=10`
    callApi("GET",TRACKS,null,handlePlaylistTrackReponse)

    playlist.classList.add('playlist');
    playlist.id = item.id;
    playlist.innerText = item.name;

    return playlist;
}

function addPlaylistTracks(item){
    let playListID = item.href.split('/')[5]
    let playlist = document.getElementById(playListID)
    let songs = document.createElement('ol')
    songs.class = 'songs'
    item.items.forEach(track => addTrack(songs,track.track.name))

    playlist.append(songs)
}

function addTrack(songs,track){
    let trackElement = document.createElement('li')
    trackElement.innerText = track

    songs.appendChild(trackElement)
}

function handlePlaylistTrackReponse(){
    if ( this.status == 200 ){
        var data = JSON.parse(this.responseText);
        addPlaylistTracks(data)
    }
    else if ( this.status == 401 ){
        refreshAccessToken()
    }
    else {
        console.log(this.responseText);
        alert(this.responseText);
    }
}

function displayUsername(username){
    const userProfile = document.querySelectorAll('.userProfile')
    
    userProfile.forEach(userProfile =>{
        userProfile.firstChild.innerText = 'Logged in as ' + username 
        localStorage.setItem("username", username);
    })
}

function handleCurrentUserResponse(){
    if ( this.status == 200 ){
        var data = JSON.parse(this.responseText);
        displayUsername(data.display_name)
    }
    else if ( this.status == 401 ){
        refreshAccessToken()
    }
    else {
        console.log(this.responseText);
        alert(this.responseText);
    }
}

function createCover(cover, item) {
    cover.classList.add('cover');
    cover.style.width = '200px';
    cover.style.height = '200px';
    if (item.images.length != 0) {
        cover.src = item.images[0].url;
    }
    return cover;
}

function refreshAccessToken(){
    refresh_token = localStorage.getItem("refresh_token");
    let body = "grant_type=refresh_token";
    body += "&refresh_token=" + refresh_token;
    body += "&client_id=" + clientId;
    callAuthorizationAPI(body);
}

function navigateToPastPlaylistPage(){
    let inputPageContainer = document.getElementById('inputPageContainer');
    inputPageContainer.style.display = 'none'
    let pastPlaylistContainer = document.getElementById('pastPlaylistContainer')
    pastPlaylistContainer.style.display = 'grid';
    populatePastPlaylistPage()
}

function navigateToMainPage(e){
    let inputPageContainer = document.getElementById('inputPageContainer');
    inputPageContainer.style.display = 'grid'
    let pastPlaylistContainer = document.getElementById('pastPlaylistContainer')
    pastPlaylistContainer.style.display = 'none';
}

function populatePastPlaylistPage(){
    let playlistWrapper = document.getElementById('playlistWrapper')
    if(!playlistWrapper.hasChildNodes()){
        callApi("GET",PLAYLISTS,null,handlePlaylistResponse)
    }
}

function translateToURIs(tracks){
    let URIstring = ''
    for (let i = 0; i< tracks.items.length; i++){
        URIstring += tracks.items[i].track.uri + ','
    }
    callApi(
    "POST",
    localStorage.getItem("newPlaylistId") + `/tracks?uris=${URIstring}`,
    null,
    addTracksToNewPlaylist)
}



function addTracksToNewPlaylist(){
    if ( this.status == 201 ){
        var data = JSON.parse(this.responseText);
        console.log(data)
        
    }
    else if ( this.status == 401 ){
        refreshAccessToken()
    }
    else {
        console.log(this.responseText);
        alert(this.responseText);
    }
}

function handleGetTracksResponse(){
    if ( this.status == 200 ){
        var data = JSON.parse(this.responseText);
        console.log(data)
        translateToURIs(data.tracks)
    }
    else if ( this.status == 401 ){
        refreshAccessToken()
    }
    else {
        console.log(this.responseText);
        alert(this.responseText);
    }
}

function handleCreatePlaylistReponse(){
    if ( this.status == 201 ){
        let imageLink = document.getElementById("imageLink").files[0]
        var data = JSON.parse(this.responseText);
        getWeatherByZip(localStorage.getItem('zip'))
        selectedWeather = localStorage.getItem('url')    
        localStorage.setItem("newPlaylistId", data.href)
        callApi("GET",selectedWeather,null,handleGetTracksResponse)
    }
    else if ( this.status == 401 ){
        refreshAccessToken()
    }
    else {
        console.log(this.responseText);
        alert(this.responseText);
    }
}

function handlePlaylistImageResponse(){
    if ( this.status == 200 ){
        console.log(this.responseText);
        alert(this.responseText);
    }
    else if ( this.status == 401 ||this.status == 400 ){
        refreshAccessToken()
        console.log(this.responseText)
    }
    else {
        console.log(this.responseText);
        alert(this.responseText);
    }
}

function createPlaylistInformation(){
    
    let playlistName = document.getElementById("playlistName").value
    let playlistJson = 
    JSON.stringify({
    "name": playlistName,
    "description": "Generated by TempestTunes.com",
    "public": false
    })
    callApi("POST",PLAYLISTS,playlistJson,handleCreatePlaylistReponse)
    callApi("PUT",localStorage.getItem("newPlaylistId") + `/images`,imageLink,handlePlaylistImageResponse)
    
}

const openModalButtons = document.querySelectorAll('[data-modal-target]');
const closeModalButtons = document.querySelectorAll('[data-close-button]');
const overlay = document.getElementById('overlay');
const nextButton = document.getElementById("nextbutton");

nextButton.addEventListener('click', () =>{
    localStorage.setItem('zip', document.getElementById('zipCodes').value)

    
    document.getElementById('nextbutton').removeChild(document.getElementById('nextbutton').getElementsByTagName('div')[0]);
    document.getElementById('insert').removeChild(document.getElementById('insert').getElementsByClassName('zipCode')[0])
    generateInput()
})

const generateInput = () => {
    const input = document.createElement("select")
    const label = document.createElement("label")
    const opt1 = document.createElement("option")
    const opt2 = document.createElement("option")
    const opt3 = document.createElement("option")

    opt1.innerText = 'Happy'
    opt2.innerText = 'Sad'
    opt3.innerText = 'Angry'
    opt1.value = '1'
    opt2.value = '2'
    opt3.value = '3'

    input.appendChild(opt1)
    input.appendChild(opt2)
    input.appendChild(opt3)
    input.id = 'selectMood'

    document.getElementById('submitButton').classList.remove('hidden')

    label.innerText = `What does the weather make you feel like?`
    
    document.getElementById('nextbutton').classList.remove('nextButton')
    document.getElementById('nextbutton').classList.add('input')
    document.getElementById('nextbutton').appendChild(label)
    document.getElementById('nextbutton').appendChild(input)
}

openModalButtons.forEach(button =>{
        button.addEventListener('click', () =>{
            const modal = document.querySelector(button.dataset.modalTarget)
            openModal(modal)
    })
})

closeModalButtons.forEach(button =>{
    button.addEventListener('click', () =>{
        const modal = button.closest('.modal')
        closeModal(modal)
    })
})

function openModal(modal){
    if (modal == null) return
    modal.classList.add('active')
    overlay.classList.add('active')
}

function closeModal(modal){
    if (modal == null) return
    modal.classList.remove('active')
    overlay.classList.remove('active')
}

overlay.addEventListener('click', () =>{
    const modals = document.querySelectorAll('.modal.active')
    modals.forEach(modal => {
        closeModal(modal)
    })
})

let inputElement = document.getElementById("imageLink")

async function getWeatherByZip(zipCode) {
    let weatherKey = 'fed200574f31448d3c4ef74409fc60bf';

    const response = await fetch(
        `https://api.openweathermap.org/data/2.5/weather?zip=${zipCode},us&appid=${weatherKey}&units=imperial`
    )
    
    const data = await response.json()
    determineWeather(data)
}


function determineWeather(data){
    let select = document.getElementById("selectMood");
    console.log(data.main.temp_max)
    let value = Number(select.value);
   

    if(value === 1){
        if (data.main.temp_max > 80 && data.clouds.all === 0 && data.main.weather[0] !== 'windy'){
            localStorage.setItem(
                'weather', 'sunny'            
            )
            localStorage.setItem(
                'url', HHOT            
            )
        } else if (data.main.weather[0] === 'snowy' && data.main.temp_max < 50){
            localStorage.setItem(
                'weather', 'winter'            
            )
            localStorage.setItem(
                'url', HWINTER            
            )
        } else if (data.main.weather[0] === 'rain'){
            localStorage.setItem(
                'weather', 'rain'            
            )
            localStorage.setItem(
                'url', HRAIN            
            )
        } else if (data.main.weather[0] === 'windy'){
            localStorage.setItem(
                'weather', 'windy'            
            )
            localStorage.setItem(
                'url', HWINDY            
            )
        }
    }else if(value === 2){
        if (data.main.temp_max > 80 && data.clouds.all === 0 && data.main.weather[0] !== 'windy'){
            localStorage.setItem(
                'weather', 'sunny'            
            )
            localStorage.setItem(
                'url', SHOT            
            )
        } else if (data.main.weather[0] === 'snowy' && data.main.temp_max < 50){
            localStorage.setItem(
                'weather', 'winter'            
            )
            localStorage.setItem(
                'url', SWINTER            
            )
        } else if (data.main.weather[0] === 'rain'){
            localStorage.setItem(
                'weather', 'rain'            
            )
            localStorage.setItem(
                'url', SRAIN            
            )
        } else if (data.main.weather[0] === 'windy'){
            localStorage.setItem(
                'weather', 'windy'            
            )
            localStorage.setItem(
                'url', SWINDY            
            )
        }
    }else if(value === 3){
        if (data.main.temp_max > 80 && data.clouds.all === 0 && data.main.weather[0] !== 'windy'){
            localStorage.setItem(
                'weather', 'sunny'            
            )
            localStorage.setItem(
                'url', AHOT            
            )
        } else if (data.main.weather[0] === 'snowy' && data.main.temp_max < 50){
            localStorage.setItem(
                'weather', 'winter'            
            )
            localStorage.setItem(
                'url', AWINTER            
            )
        } else if (data.main.weather[0] === 'rain'){
            localStorage.setItem(
                'weather', 'rain'            
            )
            localStorage.setItem(
                'url', ARAIN            
            )
        } else if (data.main.weather[0] === 'windy'){
            localStorage.setItem(
                'weather', 'windy'            
            )
            localStorage.setItem(
                'url', AWINDY            
            )
        }
    }
}
