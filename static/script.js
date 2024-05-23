document.getElementById("submit-button").addEventListener("click", function () {
    const fileInput = document.getElementById("imageInput").files[0];
    if (fileInput) {
        const formData = new FormData();
        formData.append("image", fileInput);

        fetch("/calculate_size", {
            method: "POST",
            body: formData,
        })
        .then((response) => response.text())
        .then((monument) => {
            document.getElementById("result").textContent = `Identified Monument: ${monument}`;
        })
        .catch((error) => {
            console.error("Error:", error);
        });
    } else {
        alert("Please select an image to predict the monument.");
    }
});
