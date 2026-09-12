const fileInput = document.getElementById("fileInput");

const uploadArea = document.getElementById("uploadArea");

const browseBtn = document.getElementById("browseBtn");

const changeBtn = document.getElementById("changeBtn");

const analyzeBtn = document.getElementById("analyzeBtn");

const previewContainer =
    document.getElementById("previewContainer");

const imagePreview =
    document.getElementById("imagePreview");

const fileName =
    document.getElementById("fileName");

const fileSize =
    document.getElementById("fileSize");

const resultPlaceholder =
    document.getElementById("resultPlaceholder");

const resultContent =
    document.getElementById("resultContent");

const prediction =
    document.getElementById("prediction");

const confidence =
    document.getElementById("confidence");

const confidenceBar =
    document.getElementById("confidenceBar");

const resultStatus =
    document.getElementById("resultStatus");

const resultIcon =
    document.getElementById("resultIcon");

const analyzeText =
    document.getElementById("analyzeText");

const loader =
    document.getElementById("loader");

const warning =
    document.getElementById("warning");


let selectedFile = null;


/* Open file browser */

browseBtn.addEventListener(
    "click",
    function () {

        fileInput.click();

    }
);


/* Upload area click */

uploadArea.addEventListener(
    "click",
    function (event) {

        if (
            event.target !== browseBtn
        ) {

            fileInput.click();

        }

    }
);


/* File selected */

fileInput.addEventListener(
    "change",
    function () {

        if (this.files.length > 0) {

            handleFile(
                this.files[0]
            );

        }

    }
);


/* Change button */

changeBtn.addEventListener(
    "click",
    function () {

        fileInput.click();

    }
);


/* Drag over */

uploadArea.addEventListener(
    "dragover",
    function (event) {

        event.preventDefault();

        uploadArea.classList.add(
            "dragging"
        );

    }
);


/* Drag leave */

uploadArea.addEventListener(
    "dragleave",
    function () {

        uploadArea.classList.remove(
            "dragging"
        );

    }
);


/* Drop */

uploadArea.addEventListener(
    "drop",
    function (event) {

        event.preventDefault();

        uploadArea.classList.remove(
            "dragging"
        );

        const files =
            event.dataTransfer.files;

        if (files.length > 0) {

            handleFile(files[0]);

        }

    }
);


/* Handle file */

function handleFile(file) {

    if (!file.type.startsWith("image/")) {

        alert(
            "Please select a valid MRI image."
        );

        return;

    }


    selectedFile = file;


    const reader =
        new FileReader();


    reader.onload =
        function (event) {

            imagePreview.src =
                event.target.result;

        };


    reader.readAsDataURL(file);


    fileName.textContent =
        file.name;


    fileSize.textContent =
        formatFileSize(file.size);


    uploadArea.style.display =
        "none";


    previewContainer.style.display =
        "flex";


    analyzeBtn.disabled =
        false;


    resetResult();

}


/* File size */

function formatFileSize(bytes) {

    if (bytes < 1024) {

        return bytes + " B";

    }


    if (bytes < 1024 * 1024) {

        return (
            (bytes / 1024).toFixed(1)
            + " KB"
        );

    }


    return (
        (bytes / (1024 * 1024)).toFixed(1)
        + " MB"
    );

}


/* Analyze */

analyzeBtn.addEventListener(
    "click",
    async function () {

        if (!selectedFile) {

            return;

        }


        const formData =
            new FormData();

        formData.append(
            "file",
            selectedFile
        );


        analyzeBtn.disabled =
            true;


        analyzeText.style.display =
            "none";


        loader.style.display =
            "inline-block";


        try {

            const response =
                await fetch(
                    "/predict",
                    {
                        method: "POST",
                        body: formData
                    }
                );


            if (!response.ok) {

                throw new Error(
                    "Prediction failed"
                );

            }


            const data =
                await response.json();


            showResult(data);


        }

        catch (error) {

            console.error(error);

            alert(
                "Unable to analyze the MRI image. Please try again."
            );

        }

        finally {

            analyzeBtn.disabled =
                false;

            analyzeText.style.display =
                "inline";

            loader.style.display =
                "none";

        }

    }
);


/* Show result */

function showResult(data) {

    resultPlaceholder.style.display =
        "none";


    resultContent.style.display =
        "block";


    prediction.textContent =
        data.display_class;


    confidence.textContent =
        data.confidence + "%";


    confidenceBar.style.width =
        data.confidence + "%";


    /*
       No Tumor = green
       Tumor classes = red
    */

    if (
        data.predicted_class ===
        "notumor"
    ) {

        resultStatus.classList.remove(
            "danger"
        );

        resultIcon.textContent =
            "✓";

        warning.textContent =
            "✓ AI prediction indicates no tumor detected. This result is for research and educational purposes only and is not a medical diagnosis.";

    }

    else {

        resultStatus.classList.add(
            "danger"
        );

        resultIcon.textContent =
            "!";

        warning.textContent =
            "⚠️ Possible tumor detected. Please consult a qualified medical professional for proper diagnosis and evaluation.";

    }

}


/* Reset result */

function resetResult() {

    resultPlaceholder.style.display =
        "flex";


    resultContent.style.display =
        "none";


    confidenceBar.style.width =
        "0%";

}


/* Initial state */

resetResult();