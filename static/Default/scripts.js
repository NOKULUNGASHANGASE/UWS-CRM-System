 
      // Mobile menu toggle
      const menuToggle = document.getElementById("menuToggle");
      const sidebar = document.getElementById("sidebar");

      menuToggle.addEventListener("click", () => {
        sidebar.classList.toggle("active");
      });

      // Close sidebar when clicking outside on mobile
      document.addEventListener("click", (e) => {
        if (window.innerWidth <= 768) {
          if (!sidebar.contains(e.target) && !menuToggle.contains(e.target)) {
            sidebar.classList.remove("active");
          }
        }
      });

      // Animate stats on load
      window.addEventListener("load", () => {
        const stats = document.querySelectorAll(".stat-details h3");
        stats.forEach((stat) => {
          const finalValue = stat.textContent;
          stat.textContent = "0";

          // Simple animation
          setTimeout(() => {
            stat.textContent = finalValue;
          }, 300);
        });
      });