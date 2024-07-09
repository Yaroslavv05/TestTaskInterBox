
<div class="container">
    <h2>Інструкція по запуску</h2>
    <ol>
        <li>Клонуйте репозиторій до себе на комп'ютер:
            <pre><code>git clone &lt;URL вашого репозиторію&gt;
cd &lt;ім'я папки вашого репозиторію&gt;</code></pre>
        </li>
        <li>Побудуйте Docker образ:
            <pre><code>docker build -t task_runner .</code></pre>
        </li>
        <li>Запустіть контейнер із задачею з eBay:
            <pre><code>docker run --rm task_runner ebay</code></pre>
        </li>
        <li>Запустіть контейнер із задачею отримання даних про країни:
            <pre><code>docker run --rm task_runner country</code></pre>
        </li>
        <li>Запустіть обидві задачі по черзі:
            <pre><code>docker run --rm task_runner both</code></pre>
        </li>
    </ol>
</div>

