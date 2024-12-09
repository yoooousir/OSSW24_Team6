Technical Overview
===================

Architecture
------------
This GitHub blog project, developed with the minimalistic "Jekyll-YAMT" theme, is designed to be simple, scalable, and easy to customize. The project organizes content into distinct pages, including "Home," "About," "Contact," "Community," and "Get Jekyll-Theme." It follows a modular directory structure that leverages the "Jekyll-YAMT" theme's minimalist design philosophy. 

The structure is as follows:
1. **Pages Directory:** Contains markdown files for individual pages, processed by Jekyll into static HTML.
2. **Layouts Directory:** Utilizes theme-specific layouts, such as `default.html`, to provide cohesive styling across the blog.
3. **Includes Directory:** Stores partial HTML snippets (e.g., headers and footers) optimized for the "Jekyll-YAMT" theme.
4. **Assets Directory:** Contains CSS, JavaScript, and image resources customized to align with the minimalistic aesthetics of "Jekyll-YAMT."

The design principles include:
1. **Minimalistic Design:** Leveraging "Jekyll-YAMT" to prioritize clean visuals and responsive UI.
2. **Customization-Friendly:** Facilitating straightforward adjustments to themes, colors, and layouts.
3. **Performance Optimization:** Using lightweight resources and caching mechanisms for faster page loading.

Components
----------
1. **Component One: Page Management**
   - **Purpose:** Manages the creation and navigation of pages, such as "Home," "About," "Contact," "Community," and "Get Jekyll-Theme."
   - **Implementation:** Pages are defined as markdown files in the root directory, processed by Jekyll to generate responsive, static HTML. Navigation menus leverage the theme's built-in support for dynamic rendering using the `site.pages` variable.
   - **Dependencies:** Jekyll core, "Jekyll-YAMT" theme, YAML configuration for metadata.

2. **Component Two: Theme and Layout**
   - **Purpose:** Implements the "Jekyll-YAMT" theme to achieve a cohesive and visually appealing layout.
   - **Implementation:** Uses the theme’s predefined layout files for uniformity. Custom styles are added via the `assets/css/style.css` file to fine-tune the appearance while adhering to the minimalistic approach.
   - **Dependencies:** SCSS for styling, Jekyll's Liquid templating engine, and "Jekyll-YAMT" as the primary theme.

Technology Stack
----------------
- **Languages:** Ruby, HTML5, CSS3, JavaScript
- **Framework:** Jekyll
- **Theme:** Jekyll-YAMT
- **Version Control:** Git, GitHub
- **Development Tools:** Visual Studio Code (VSCode), Ruby Gems for dependency management
- **Testing Tools:** 
  - HTML Validators for semantic correctness.
  - Lighthouse for performance, accessibility, and SEO audits.

By integrating the "Jekyll-YAMT" theme with a modular structure and robust tools, this project delivers a clean and efficient blogging platform with strong customization options.
