const trash = document.querySelectorAll('.fa-trash');

    for (i=0; i<trash.length; i++){
        trash[i].addEventListener('click', (e) => {
            
            let primaryKey = e.target.parentElement.parentElement.parentElement.firstElementChild.textContent;

            fetch(`http://127.0.0.1:8000/delete/${primaryKey}`, {method : 'DELETE'})
                .then((data) => {
                    if (data['status'] === 204) {
                        window.location.reload();
                    }   
                });
            }
        );
    }

    const update = document.querySelectorAll('.fa-pencil');
    let storeInput = document.getElementById('store');
    let skuInput = document.getElementById('sku');
    let priceInput = document.getElementById('price');
    let productInput = document.getElementById('product');
    let dateInput = document.getElementById('date');
    let toBeUpdated;

    for (i=0; i<update.length; i++){
        update[i].addEventListener('click', (e) => {

            let dateValue = e.target.parentElement.parentElement.previousElementSibling.textContent;

            let priceValue = e.target.parentElement.parentElement.previousElementSibling.previousElementSibling.textContent;

            let productValue = e.target.parentElement.parentElement.previousElementSibling.previousElementSibling.previousElementSibling.textContent;

            let skuValue = e.target.parentElement.parentElement.previousElementSibling.previousElementSibling.previousElementSibling.previousElementSibling.textContent;

            let storeValue = e.target.parentElement.parentElement.previousElementSibling.previousElementSibling.previousElementSibling.previousElementSibling.previousElementSibling.textContent;

            toBeUpdated = e.target.parentElement.parentElement.previousElementSibling.previousElementSibling.previousElementSibling.previousElementSibling.previousElementSibling.previousElementSibling.textContent;

            storeInput.value = '';
            skuInput.value = '';
            priceInput.value = '';
            productInput.value = '';
            dateInput.value = '';

            storeInput.value = storeValue;
            skuInput.value = skuValue;
            priceInput.value = priceValue.slice(1);
            productInput.value = productValue;

            dateFormat = new Date(dateValue)

            let month = String(dateFormat.getMonth()+1).length == 1 ? `0${String(dateFormat.getMonth()+1)}` : dateFormat.getMonth()+1;

            let date = String(dateFormat.getDate()).length == 1 ? `0${String(dateFormat.getDate())}` : dateFormat.getDate();

            dateValue = `${dateFormat.getFullYear()}-${month}-${date}`;
            dateInput.value = dateValue;

            }
        );
    }

    const updateButton = document.getElementById('update-button');
    
    updateButton.addEventListener('click', (e) => {

        const requestOptions = {
            method: 'PUT',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ 
                store : storeInput.value,
                sku : skuInput.value,
                product : productInput.value,
                price : priceInput.value,
                date : dateInput.value
            })
        };          
        fetch(`http://127.0.0.1:8000/update/${Number(toBeUpdated)}`, requestOptions)
            .then(result => {
                if (result['status'] === 201) {
                    window.location.reload();
                }else{
                    alert('please check the data being updated');
                }
            })
        }
    );

    const searchReset = document.getElementById('reset-search');
    const updateReset = document.getElementById('reset-button');

    searchReset.addEventListener('click', (e) => {
            window.location.href = window.location.href.split('?')[0];
        }
    );

    updateReset.addEventListener('click', (e) => {
        window.location.href = window.location.href.split('?')[0];
        storeInput.value = '';
        skuInput.value = '';
        priceInput.value = '';
        productInput.value = '';
        dateInput.value = '';
        toBeUpdated = '';
        }
    );