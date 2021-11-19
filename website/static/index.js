function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }

  function deleteListing(listingId) {
    fetch("/delete-listing", {
      method: "POST",
      body: JSON.stringify({ listingId: listingId }),
    }).then((_res) => {
      window.location.href = "/listings";
    });
  }