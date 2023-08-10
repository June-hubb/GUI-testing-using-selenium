function addGenre() {
    // Get the value of the input field
    let genre = document.getElementById("favorite-genre").value.trim();
    
    // If the input field is not empty
    if (genre !== "") {
      // Create a new list item element
      let li = document.createElement("li");
      
      // Set the text of the new list item to the genre value
      li.textContent = genre;
      
      // Add the new list item to the favorite genres list
      let favoriteGenresList = document.querySelector(".profile-details ul");
      favoriteGenresList.appendChild(li);
      
      // Clear the input field
      document.getElementById("favorite-genre").value = "";
    }
  }
  function updatePreferredFormat() {
    const preferredFormat = document.querySelector('input[name="reading-format"]:checked').value;
    const displayText = `Preferred Format: ${preferredFormat.charAt(0).toUpperCase() + preferredFormat.slice(1)}`;
    document.getElementById("preferred-format-display").innerHTML = displayText;
  }
  function explore(){
  window.location.href = "explore.html";}