let page = 2;

function loadItems () {
	let main = document.querySelector("#mainer");
	let template = document.querySelector("#post_template");


	fetch(`/load?p=${page}`).then((response) => {
		response.json().then((data) => {
			let obj = data;
			obj = obj.articles
			console.log(obj);

			for (let i = 0; i < obj.length; i++)
			{
				let template_clone = template.content.cloneNode(true);
				template_clone.getElementById("head").textContent = obj[i]["source"]["name"];
				
				if (obj[i]["urlToImage"] != null){
					template_clone.querySelector("#img").src = obj[i]["urlToImage"];
				}else
				{
					let myimg = template_clone.querySelector("#img");
					myimg.remove();
				}
				
				template_clone.querySelector("#ptitle").textContent = obj[i]["title"];
				template_clone.querySelector("#des").textContent = obj[i]["description"];
				template_clone.querySelector("#lnk").href = obj[i]["url"];
				main.appendChild(template_clone);
			}
			page += 1;
		})
	})
}

function createObserver ()
{
	let sentinel = document.querySelector("#sentinel");

	let options = {
		root: null,
		rootMargin: "0px",
		threshold: 0.1
	};

	let observer = new IntersectionObserver(loadItems, options);
	observer.observe(sentinel);
}

window.addEventListener("load", (event) => {
	 

	createObserver();
}, false);