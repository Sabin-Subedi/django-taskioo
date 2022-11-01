const handlePwdIconClick = (e) => {
  const icon = document.createElement("i");
  icon.setAttribute("onclick", "handlePwdIconClick(this)");
  icon.className = "w-5 cursor-pointer text-gray-700";

  if (e.classList.contains("feather-eye")) {
    icon.setAttribute("data-feather", "eye-off");

    if (
      e.previousElementSibling.attributes.getNamedItem("type").value ===
      "password"
    ) {
      e.previousElementSibling.setAttribute("type", "text");
      e.replaceWith(icon);
      feather.replace();
    }
  } else if (e.classList.contains("feather-eye-off")) {
    icon.setAttribute("data-feather", "eye");
    if (
      e.previousElementSibling.attributes.getNamedItem("type").value === "text"
    ) {
      e.previousElementSibling.setAttribute("type", "password");
      e.replaceWith(icon);
      feather.replace();
    }
  }
};
