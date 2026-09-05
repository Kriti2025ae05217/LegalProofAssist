async function checkText() {

    const text =
        document.getElementById("text").value;

    const clause_id =
        document.getElementById(
          "clause_id"
        ).value;

    const response =
        await fetch("/check", {

        method: "POST",

        headers: {
            "Content-Type":
            "application/json"
        },

        body: JSON.stringify({
            clause_id,
            text
        })
    });

    const data =
        await response.json();

    let html = "";

    data.results.forEach(item => {

        html += `
        <tr>
        <td>${item.word}</td>
        <td>${item.suggestion}</td>
        <td>${item.error_type}</td>
        <td>${item.confidence}</td>
        </tr>
        `;
    });

    document.getElementById(
        "resultTable"
    ).innerHTML = html;
}
