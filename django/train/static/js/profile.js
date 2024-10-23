document.getElementById('profileImageInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const profileImage = document.getElementById('profileImage');
            if (profileImage) {
                profileImage.src = e.target.result;
            } else {
                // If there was no image before, replace initials with the new image
                const initialsDiv = document.querySelector('.profile-picture .initials');
                if (initialsDiv) {
                    initialsDiv.outerHTML = `<img src="${e.target.result}" alt="{{ request.user.username }}" id="profileImage">`;
                }
            }
        };
        reader.readAsDataURL(file);
    }
});
