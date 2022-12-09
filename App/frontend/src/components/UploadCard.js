import React, { useState } from "react";
import { useAuth } from "../auth/authentication";
import { HOST } from "../constants/host";
import { RiDragDropLine } from "react-icons/ri";
import { AiOutlineClose } from "react-icons/ai";

import "./styles/UploadCard.css";

function UploadCard(props) {
  const { token } = useAuth();
  var host = HOST;

  /*const [uploadInfo, setUploadInfo] = useState({
    title: "",
    description: "",
    type: "",
    tags: [],
    artitem_image: "",
  });*/

  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [type, setType] = useState("");
  const [tags, setTags] = useState([]);
  const [base64Image, setBase64Image] = useState("olmadi");

  const [preview, setPreview] = useState(false);
  const [previewImage, setPreviewImage] = useState("");

  const [isLoading, setIsLoading] = useState(false);

  // console.log(username);

  async function handlePreview(e) {
    if (e.target.files) {
      setPreview(true);
      props.setPostError(false);
      setPreviewImage(URL.createObjectURL(e.target.files[0]));
      setBase64Image(await toBase64(e.target.files[0]));
    }
  }

  function closePreview() {
    setPreview(false);
    setPreviewImage("");
    setBase64Image("");
  }

  const handleDragOver = (e) => {
    e.preventDefault();
  };

  async function handleOnDrop(e) {
    //prevent the browser from opening the image
    e.preventDefault();
    e.stopPropagation();
    //let's grab the image file
    setPreview(true);
    props.setPostError(false);
    setPreviewImage(URL.createObjectURL(e.dataTransfer.files[0]));
    setBase64Image(await toBase64(e.dataTransfer.files[0]));
  }

  function handlePost(e) {
    e.preventDefault();
    if (previewImage === "") {
      props.setPostError(true);
    } else if (title === "" || description === "" || type === "") {
      props.setUploadInfoError(true);
    } else {
      setIsLoading(true);
      fetch(`${host}/api/v1/artitems/me/upload/`, {
        method: "POST",
        body: JSON.stringify({
          title: title,
          description: description,
          type: type,
          tags: tags,
          artitem_image: base64Image,
        }),
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${token}`,
        },
      })
        .then((response) => {
          setIsLoading(false);
          props.setNewImageUploaded();
          props.closeUploadCard();

          closePreview();
          setTitle("");
          setDescription("");
          setType("");
          setTags([]);

          return response.json();
        })
        .then((response) => {
          // console.log(response);
        })
        .catch((error) => console.error("Error:", error));
    }
  }

  const toBase64 = (file) =>
    new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => resolve(reader.result);
      reader.onerror = (error) => reject(error);
    });

  function handleTitle(e) {
    const value = e.target.value;
    setTitle(value);
  }

  function handleDescription(e) {
    const value = e.target.value;
    setDescription(value);
  }

  function handleType(e) {
    const value = e.target.value;
    setType(value);
  }

  function handleTags(e) {
    const value = e.target.value;
    setTags([]);
  }

  return (
    <div
      className="upload-container"
      style={{
        height: props.height,
        border: props.border,
        marginBottom: props.marginBottom,
      }}
    >
      <div
        className="upload-container-loading"
        style={{ visibility: isLoading ? "visible" : "hidden" }}
      >
        <div
          class="spinner-border"
          style={{
            width: "6rem",
            height: "6rem",
            color: "black",
          }}
          role="status"
        >
          <span class="sr-only"></span>
        </div>
      </div>
      <div
        className="upload-grid"
        style={{ display: props.height === "0px" ? "none" : "grid" }}
      >
        <div
          className="upload-interface-container"
          style={{ cursor: preview ? "default" : "pointer" }}
          onDragOver={handleDragOver}
          onDrop={handleOnDrop}
        >
          {!preview ? (
            <div style={{ textAlign: "center" }}>
              <header className="upload-interface-header">
                Upload an art item
              </header>
              <label className="btn upload-interface-btn" htmlFor="art-item">
                Select from files
              </label>
              <input
                type="file"
                className="mt-1"
                name="art-item"
                id="art-item"
                accept="image/*"
                onChange={handlePreview}
              />
              <div style={{ color: "#bcb1c1", marginBottom: "0.2rem" }}>or</div>
              <div style={{ color: "#bcb1c1" }}>
                <RiDragDropLine style={{ marginBottom: "0.1rem" }} /> drag and
                drop here
              </div>
              {props.postError && (
                <div className="upload-post-error">
                  Please select an art item
                </div>
              )}
            </div>
          ) : (
            <div className="upload-post-preview-container">
              <div className="upload-post-wrap">
                <img
                  src={previewImage}
                  alt=""
                  className="upload-post-preview"
                  id="upload-post-preview"
                />
                <div className="upload-post-cancel-container">
                  <AiOutlineClose
                    className="upload-post-cancel-btn"
                    onClick={closePreview}
                  ></AiOutlineClose>
                </div>
              </div>
            </div>
          )}
        </div>
        <form className="upload-info">
          <header className="upload-info-header">
            Provide details about your art item and increase the chances of
            being discovered
          </header>

          {props.uploadInfoError && (
            <div className="upload-info-error">
              Title, description and category fields may not be left blank.
            </div>
          )}

          <div className="form-group mt-4">
            <label className="access-label" style={{ color: "#ffc9ff" }}>
              Title
            </label>
            <input
              type="text"
              className="form-control mt-1"
              placeholder="Give a title"
              name="title"
              id="title"
              style={{ fontSize: "14px" }}
              value={title}
              onChange={handleTitle}
            />
          </div>
          <div className="form-group mt-3">
            <label className="access-label" style={{ color: "#ffc9ff" }}>
              Description
            </label>
            <textarea
              type="text"
              className="form-control mt-1"
              placeholder="Describe your art item"
              name="description"
              id="description"
              style={{ fontSize: "14px", resize: "none" }}
              rows="2"
              value={description}
              onChange={handleDescription}
            />
          </div>
          <div className="form-group mt-3">
            <label className="access-label" style={{ color: "#ffc9ff" }}>
              Category
            </label>
            <input
              type="text"
              className="form-control mt-1"
              placeholder="Painting, photography, digital art..."
              name="type"
              id="type"
              style={{ fontSize: "14px" }}
              value={type}
              onChange={handleType}
            />
          </div>
          <div className="form-group mt-3">
            <label className="access-label" style={{ color: "#ffc9ff" }}>
              Tags
            </label>
            <input
              type="text"
              className="form-control mt-1"
              placeholder="Add tags"
              name="tags"
              id="tags"
              style={{ fontSize: "14px" }}
              value={tags}
              onChange={handleTags}
            />
          </div>

          <div className="d-grid gap-2 mt-4 mb-4">
            <button
              type="submit"
              className="btn upload-post-btn"
              onClick={handlePost}
            >
              Post
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default UploadCard;
