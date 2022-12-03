import React, { useState } from "react";
import { RiDragDropLine } from "react-icons/ri";
import { AiOutlineClose } from "react-icons/ai";

import "./styles/UploadCard.css";

function UploadCard(props) {
  const [preview, setPreview] = useState(false);
  const [previewImage, setPreviewImage] = useState("");

  function handlePreview(e) {
    if (e.target.files) {
      setPreview(true);
      props.setPostError(false);
      setPreviewImage(URL.createObjectURL(e.target.files[0]));
    }
  }

  function closePreview() {
    setPreview(false);
    setPreviewImage("");
  }

  const handleDragOver = (e) => {
    e.preventDefault();
  };

  const handleOnDrop = (e) => {
    //prevent the browser from opening the image
    e.preventDefault();
    e.stopPropagation();
    //let's grab the image file
    setPreview(true);
    props.setPostError(false);
    setPreviewImage(URL.createObjectURL(e.dataTransfer.files[0]));
  };

  function handlePost(e) {
    if (previewImage === "") {
      e.preventDefault();
      props.setPostError(true);
    }
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
              style={{ fontSize: "14px" }}
              rows="2"
            />
          </div>
          <div className="form-group mt-3">
            <label className="access-label" style={{ color: "#ffc9ff" }}>
              Category
            </label>
            <input
              type="text"
              className="form-control mt-1"
              placeholder="Painting, sculpture, digital art..."
              name="type"
              id="type"
              style={{ fontSize: "14px" }}
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
