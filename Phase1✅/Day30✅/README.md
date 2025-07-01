# Day 30

Absolutely! Let’s go through **every Tailwind CSS class used** in the full HTML example and explain them by **section**:

---

## 🧭 1. **`<body>`**

```html
<body class="bg-white text-gray-800 font-sans">
```

| Class           | Meaning                           |
| --------------- | --------------------------------- |
| `bg-white`      | Sets background color to white    |
| `text-gray-800` | Sets base text color to dark gray |
| `font-sans`     | Uses a sans-serif font family     |

---

## 🚀 2. **Navbar**

```html
<nav class="bg-black text-white px-6 py-4 flex justify-between items-center">
```

| Class             | Meaning                                        |
| ----------------- | ---------------------------------------------- |
| `bg-black`        | Navbar background color                        |
| `text-white`      | Sets text color to white                       |
| `px-6`            | Horizontal padding = 1.5rem (left and right)   |
| `py-4`            | Vertical padding = 1rem (top and bottom)       |
| `flex`            | Converts nav into a flex container             |
| `justify-between` | Puts space between logo and nav links          |
| `items-center`    | Vertically centers the items within the navbar |

```html
<ul class="flex gap-6">
```

| Class   | Meaning                                 |
| ------- | --------------------------------------- |
| `flex`  | Displays list items in a row            |
| `gap-6` | Adds spacing between nav items (1.5rem) |

```html
<a class="hover:text-gray-400">
```

| Class                 | Meaning                             |
| --------------------- | ----------------------------------- |
| `hover:text-gray-400` | Changes text color to gray on hover |

---

## 🦸 3. **Hero Section (Flexbox)**

```html
<section class="flex flex-col md:flex-row items-center justify-between px-10 py-20 bg-gray-100">
```

| Class             | Meaning                                             |
| ----------------- | --------------------------------------------------- |
| `flex`            | Makes it a flex container                           |
| `flex-col`        | Default (mobile): stack vertically                  |
| `md:flex-row`     | On medium+ screens: stack horizontally (row layout) |
| `items-center`    | Vertically centers content inside flex              |
| `justify-between` | Space between left and right content                |
| `px-10`           | Horizontal padding = 2.5rem                         |
| `py-20`           | Vertical padding = 5rem                             |
| `bg-gray-100`     | Light gray background                               |

```html
<div class="md:w-1/2 mb-10 md:mb-0">
```

| Class      | Meaning                                 |
| ---------- | --------------------------------------- |
| `md:w-1/2` | Width is 50% on medium+ screens         |
| `mb-10`    | Margin-bottom = 2.5rem (mobile)         |
| `md:mb-0`  | Remove margin-bottom on medium+ screens |

```html
<h2 class="text-4xl font-bold mb-4">
```

| Class       | Meaning              |
| ----------- | -------------------- |
| `text-4xl`  | Font size large      |
| `font-bold` | Bold font            |
| `mb-4`      | Bottom margin (1rem) |

```html
<p class="text-lg text-gray-600 mb-6">
```

| Class           | Meaning           |
| --------------- | ----------------- |
| `text-lg`       | Large text        |
| `text-gray-600` | Medium gray color |
| `mb-6`          | Bottom margin     |

```html
<a class="bg-blue-600 text-white px-6 py-3 rounded hover:bg-blue-800">
```

| Class               | Meaning                     |
| ------------------- | --------------------------- |
| `bg-blue-600`       | Dark blue background        |
| `text-white`        | White text                  |
| `px-6`              | Horizontal padding (1.5rem) |
| `py-3`              | Vertical padding (0.75rem)  |
| `rounded`           | Slightly rounded corners    |
| `hover:bg-blue-800` | Darker blue on hover        |

```html
<img class="rounded shadow-lg">
```

| Class       | Meaning                |
| ----------- | ---------------------- |
| `rounded`   | Rounded corners        |
| `shadow-lg` | Large shadow for depth |

---

## 💎 4. **Features Section (CSS Grid)**

```html
<section class="px-10 py-20 bg-white">
```

| Class      | Meaning            |
| ---------- | ------------------ |
| `px-10`    | Horizontal padding |
| `py-20`    | Vertical padding   |
| `bg-white` | White background   |

```html
<h3 class="text-3xl font-bold text-center mb-10">
```

| Class         | Meaning             |
| ------------- | ------------------- |
| `text-3xl`    | Large font size     |
| `font-bold`   | Bold font           |
| `text-center` | Center-aligned text |
| `mb-10`       | Bottom margin       |

```html
<div class="grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
```

| Class            | Meaning                            |
| ---------------- | ---------------------------------- |
| `grid`           | Activates CSS Grid                 |
| `grid-cols-1`    | 1 column on small screens          |
| `md:grid-cols-3` | 3 columns on medium+ screens       |
| `gap-8`          | Space between grid items           |
| `text-center`    | Center-aligns text inside each box |

```html
<div class="p-6 bg-gray-50 rounded-lg shadow">
```

| Class        | Meaning                               |
| ------------ | ------------------------------------- |
| `p-6`        | Padding: 1.5rem                       |
| `bg-gray-50` | Very light gray background            |
| `rounded-lg` | Large border radius (rounded corners) |
| `shadow`     | Default box shadow                    |

```html
<h4 class="text-xl font-semibold mb-2">
```

| Class           | Meaning                |
| --------------- | ---------------------- |
| `text-xl`       | Large heading size     |
| `font-semibold` | Semi-bold font         |
| `mb-2`          | Margin bottom (0.5rem) |

```html
<p class="text-gray-600">
```

| Class           | Meaning                |
| --------------- | ---------------------- |
| `text-gray-600` | Medium gray text color |

---

## 🧱 5. **Footer**

```html
<footer class="bg-black text-white text-center py-6 mt-10">
```

| Class         | Meaning             |
| ------------- | ------------------- |
| `bg-black`    | Black background    |
| `text-white`  | White text          |
| `text-center` | Centered text       |
| `py-6`        | Vertical padding    |
| `mt-10`       | Top margin (2.5rem) |

---

## ✅ Bonus Tip: How Tailwind Units Work

* `p`, `m`, `gap`, `text`, `rounded`, `shadow` all follow Tailwind's **scale system** (e.g., `p-4` = 1rem, `text-xl` = large text, etc.)
* Responsive prefixes like `md:` apply the class at `768px+`

---

If you’d like, I can make a **cheatsheet PDF** of these Tailwind classes or generate a **custom component** like a pricing card, testimonial, or product grid. Just ask!
