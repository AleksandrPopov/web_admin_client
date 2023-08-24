const add_address_btn = document.getElementById('add_address_btn');
const deleteButtons = document.querySelectorAll(".btn-delete");

add_address_btn.addEventListener('click', function () {
    alert("clicked")
});


deleteButtons.forEach(function (button) {
    button.addEventListener('click', function () {
        const elementId = this.getAttribute('data-element-id');
        if (confirm("Yes?")) {
            const xhr = new XMLHttpRequest();
            xhr.open("POST", "{% url 'address' %}", true);
            xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
            xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}")
            {
                if (xhr.readyState === 4) {
                    if (xhr.status === 200) {
                        const elementDiv = document.getElementById("element-" + elementId);
                        elementDiv.parentNode.removeChild(elementDiv);  // Remove the element from the DOM
                    } else {
                        // Handle error
                    }
                }
            }
            xhr.send("element_id=" + encodeURIComponent(elementId));
        }
    })
})