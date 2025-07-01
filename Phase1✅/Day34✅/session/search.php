<?php
if (isset($_GET['query'])) {
    $search = htmlspecialchars($_GET['query']);
    echo "<h2>You searched for: <em>$search</em></h2>";
} else {
    echo "<p>No search term entered.</p>";
}
?>
