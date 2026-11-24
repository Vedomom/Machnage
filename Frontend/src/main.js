

async function get_db_names() {
  const optionBtn = document.querySelector("#selectButton");
  await fetch(document.URL + "api/db").then(response => response.json()).then(data => {
    for (const [id, db] of Object.entries(data)){
      const db_option = document.createElement("option");
      db_option.value = db;
      db_option.innerText = db.replace(".db", "");
      optionBtn.appendChild(db_option);
    }
  })
}

async function get_names(db_name , amount) {
  const nameContainer = document.querySelector("#NameContainer");
  nameContainer.innerHTML = "";
  await fetch(document.URL + "api/gen/" + `?db_name=${db_name}&amount=${amount}`).then(response => response.json()).then(data => {
    for(const [id, name] of Object.entries(data)){
      const nameCard = document.createElement("div");
      nameCard.classList.add("nameCard")
      nameCard.innerText = name;
      nameContainer.appendChild(nameCard);
      console.log(nameCard)
    }
  })
}


const nameButton = document.querySelector("#btn");
nameButton.addEventListener("click", () => {
  get_names(optionBtn.value, amountSelect.value)
})

const optionBtn = document.querySelector("#selectButton");
const amountSelect = document.querySelector("#amount");

get_db_names()