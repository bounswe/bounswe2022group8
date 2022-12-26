import React, { useState } from "react";
import Select from "react-select";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import { useAuth } from "../auth/authentication";
import { HOST } from "../constants/host";
import { RiDragDropLine } from "react-icons/ri";
import { AiOutlineClose } from "react-icons/ai";
import ArtItemSelection from "./ArtItemSelection";
import Backdrop from "../components/Backdrop";

import "./styles/UploadCard.css";

function UploadOnlineExhibitionCard(props) {
  const { token } = useAuth();
  var host = HOST;

  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [collaborators, setCollaborators] = useState([]);
  const [startDate, setStartDate] = useState(new Date());
  const [endDate, setEndDate] = useState(new Date());
  const [base64Images, setBase64Images] = useState([]);
  const [posterBase64, setPosterBase64] = useState("");

  const [previewImages, setPreviewImages] = useState([]);
  const [posterPreview, setPosterPreview] = useState("");

  const [preview, setPreview] = useState(0);

  const [isArtItemSelectionOpen, setIsArtItemSelectionOpen] = useState(false);
  const [artItemsGallery, setArtItemsGallery] = useState([]);
  const [artItemsGalleryIndexes, setArtItemGalleryIndexes] = useState(
    Array.from(new Array(props.userGallery.length).fill(false))
  );

  const [isLoading, setIsLoading] = useState(false);

  async function handlePreview(e) {
    if (e.target.files) {
      setPreview(1);
      props.setPostError(false);

      var artitems_upload = [];
      for (let i = 0; i < e.target.files.length; i++) {
        artitems_upload.push(URL.createObjectURL(e.target.files[i]));
      }

      const base64_upload = await tobase64Handler(e.target.files);
      // console.log(base64_upload);

      setPreviewImages([...previewImages, ...artitems_upload]);
      setBase64Images([...base64Images, ...base64_upload]);
    }
  }

  function cancelGalleryArtItem(id, index) {
    const copy = [...artItemsGalleryIndexes];
    copy[index] = !artItemsGalleryIndexes[index];
    setArtItemGalleryIndexes(copy);

    setArtItemsGallery((current) =>
      current.filter((currentElement) => currentElement !== id)
    );

    // if there is only one art item left to be deleted
    if (artItemsGallery.length === 1 && previewImages.length === 0) {
      setPreview(0);
    }
  }

  function cancelUploadedArtItem(index) {
    const copy_1 = [...previewImages];
    copy_1.splice(index, 1);
    setPreviewImages(copy_1);

    const copy_2 = [...base64Images];
    copy_2.splice(index, 1);
    setBase64Images(copy_2);

    // if there is only one art item left to be deleted
    if (previewImages.length === 1 && artItemsGallery.length === 0) {
      setPreview(0);
    }
  }

  function handleArtItemSelection() {
    setIsArtItemSelectionOpen(true);
  }

  const handleDragOver = (e) => {
    e.preventDefault();
  };

  async function handleOnDrop(e) {
    //prevent the browser from opening the image
    e.preventDefault();
    e.stopPropagation();
    //let's grab the image file
    setPreview(1);
    props.setPostError(false);
    setPreviewImages((current) => [
      ...current,
      URL.createObjectURL(e.dataTransfer.files[0]),
    ]);
    let base64 = await toBase64(e.dataTransfer.files[0]);
    setBase64Images((current) => [...current, base64]);
  }

  async function handlePoster(e) {
    if (e.target.files) {
      setPreview(2);
      props.setPostError(false);
      setPosterPreview(URL.createObjectURL(e.target.files[0]));
      setPosterBase64(await toBase64(e.target.files[0]));
    }
  }

  function handleRemoveAll() {
    setPreview(0);
    props.setPostError(false);
    setPreviewImages([]);
    setBase64Images([]);
    setArtItemsGallery([]);
    setArtItemGalleryIndexes(
      Array.from(new Array(props.userGallery.length).fill(false))
    );
  }

  function closePoster() {
    setPreview(1);
    setPosterPreview("");
    setPosterBase64("");
  }

  function handlePost(e) {
    e.preventDefault();
    if (previewImages.length === 0 && artItemsGallery.length === 0) {
      props.setPostError(true);
    } else if (title === "" || description === "" || posterPreview === "") {
      props.setUploadInfoError(true);
    } else {
      const temp = base64Images.map((base64) => ({
        title: title,
        description: `This art item is part of the ${title} exhibition and was uploaded exclusively for this exhibition`,
        tags: [],
        category: "OT",
        artitem_image: base64,
      }));

      console.log(temp);
      setIsLoading(true);
      fetch(`${host}/api/v1/exhibitions/me/online/`, {
        method: "POST",
        body: JSON.stringify({
          title: title,
          description: description,
          collaborators: collaborators.map(({ value }) => value),
          start_date: startDate,
          end_date: endDate,
          artitems_gallery: artItemsGallery,
          artitems_upload: base64Images.map((base64) => ({
            title: title,
            description: `This art item is part of the ${title} exhibition and was uploaded exclusively for this exhibition`,
            tags: [],
            category: "OT",
            artitem_image: base64,
          })),
          poster: posterBase64,
        }),
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${token}`,
        },
      })
        .then((response) => {
          setIsLoading(false);
          props.setNewOnlineExhibitionUploaded();
          props.closeUploadOnlineExhibitionCard();

          setTitle("");
          setDescription("");
          setCollaborators([]);
          setStartDate(new Date());
          setEndDate(new Date());
          setPosterPreview("");
          setPosterBase64("");
          handleRemoveAll();
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

  async function tobase64Handler(files) {
    const filePathsPromises = [];

    Array.from(files).forEach((file) => {
      filePathsPromises.push(toBase64(file));
    });

    const filePaths = await Promise.all(filePathsPromises);
    return filePaths;
  }

  function handleTitle(e) {
    const value = e.target.value;
    setTitle(value);
  }

  function handleDescription(e) {
    const value = e.target.value;
    setDescription(value);
  }

  function handleCollaborators(selectedOptions) {
    setCollaborators(selectedOptions);
  }

  function handleOnClickAdd(selectedArtItems, selectedArtItemIndexes) {
    if (selectedArtItems.length !== 0) {
      setArtItemsGallery(selectedArtItems);
      setArtItemGalleryIndexes(selectedArtItemIndexes);
      setPreview(1);
    } else {
      setPreview(0);
    }

    setIsArtItemSelectionOpen(false);
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
          {isArtItemSelectionOpen && (
            <>
              <ArtItemSelection
                onClickCancel={() => setIsArtItemSelectionOpen(false)}
                onClickAdd={(selectedArtItems, selectedArtItemIndexes) =>
                  handleOnClickAdd(selectedArtItems, selectedArtItemIndexes)
                }
                userGallery={props.userGallery}
                artItemsGallery={artItemsGallery}
                artItemsGalleryIndexes={artItemsGalleryIndexes}
              />
              <Backdrop onClick={() => setIsArtItemSelectionOpen(false)} />
            </>
          )}

          {preview === 0 && (
            <div style={{ textAlign: "center" }}>
              <header
                className="upload-interface-header"
                style={{ marginTop: "10rem" }}
              >
                Organise an online exhibition
              </header>
              <div style={{ marginTop: "0.25rem" }}>
                Select the art items you want to include in your exhibition
              </div>
              <div className="upload-interface-buttons">
                <label
                  className="btn upload-interface-btn"
                  htmlFor="select-art-item-from-file"
                >
                  Select from files
                </label>
                <input
                  type="file"
                  className="mt-1"
                  name="select-art-item-from-file"
                  id="select-art-item-from-file"
                  accept="image/*"
                  multiple
                  onChange={handlePreview}
                />
                <button
                  className="btn upload-interface-btn"
                  onClick={handleArtItemSelection}
                >
                  Select from gallery
                </button>
              </div>
              <div
                style={{
                  color: "#bcb1c1",
                  marginBottom: "0.2rem",
                  marginRight: "1.23rem",
                }}
              >
                or
              </div>
              <div style={{ color: "#bcb1c1", marginRight: "1.23rem" }}>
                <RiDragDropLine style={{ marginBottom: "0.1rem" }} /> drag and
                drop here
              </div>
              {props.postError && (
                <div className="upload-post-error">
                  Please select an art item
                </div>
              )}
            </div>
          )}
          {preview === 1 && (
            <>
              <div className="upload-exhibition-preview-container">
                {previewImages.map((val, index) => {
                  return (
                    <div key={val} className="upload-exhibition-wrap">
                      <img
                        src={val}
                        alt=""
                        className="upload-exhibition-preview"
                      />
                      <div className="upload-post-cancel-container">
                        <AiOutlineClose
                          className="upload-post-cancel-btn"
                          onClick={() => cancelUploadedArtItem(index)}
                          style={{
                            top: "0.3rem",
                            right: "0.3rem",
                            fontSize: "18px",
                          }}
                        ></AiOutlineClose>
                      </div>
                    </div>
                  );
                })}
                {props.userGallery.map((val, index) => {
                  return (
                    <div
                      key={val.id}
                      className="upload-exhibition-wrap"
                      style={{
                        display: artItemsGalleryIndexes[index]
                          ? "block"
                          : "none",
                      }}
                    >
                      <img
                        src={val.artitem_path}
                        alt={val.description}
                        className="upload-exhibition-preview"
                      />
                      <div className="upload-post-cancel-container">
                        <AiOutlineClose
                          className="upload-post-cancel-btn"
                          onClick={() => cancelGalleryArtItem(val.id, index)}
                          style={{
                            top: "0.3rem",
                            right: "0.3rem",
                            fontSize: "18px",
                          }}
                        ></AiOutlineClose>
                      </div>
                    </div>
                  );
                })}
              </div>
              <div
                style={{
                  display: "flex",
                  justifyContent: "space-between",
                  gap: "1rem",
                  margin: "-3rem 2rem 2rem 2rem",
                }}
              >
                <button
                  className="btn upload-interface-btn"
                  onClick={handleRemoveAll}
                >
                  Remove all selected
                </button>
                <label
                  className="btn upload-interface-btn"
                  htmlFor="add-art-items-from-file"
                >
                  Add from files
                </label>
                <input
                  type="file"
                  className="mt-1"
                  name="add-art-items-from-file"
                  id="add-art-items-from-file"
                  accept="image/*"
                  multiple
                  onChange={handlePreview}
                />
                <button
                  className="btn upload-interface-btn"
                  onClick={handleArtItemSelection}
                >
                  Add from gallery
                </button>
                <label
                  className="btn upload-interface-btn"
                  htmlFor="add-poster-from-file"
                >
                  Save and select poster
                </label>
                <input
                  type="file"
                  className="mt-1"
                  name="add-poster-from-file"
                  id="add-poster-from-file"
                  accept="image/*"
                  onChange={handlePoster}
                />
              </div>
            </>
          )}
          {preview === 2 && (
            <div className="upload-post-preview-container">
              <div className="upload-post-wrap">
                <img
                  src={posterPreview}
                  alt=""
                  className="upload-poster-preview"
                  id="upload-poster-preview"
                />
                <div className="upload-post-cancel-container">
                  <AiOutlineClose
                    className="upload-post-cancel-btn"
                    onClick={closePoster}
                  ></AiOutlineClose>
                </div>
              </div>
            </div>
          )}
        </div>

        <form className="upload-info">
          <header className="upload-info-header">
            Enter the necessary information about your exhibition and make sure
            it reaches more people
          </header>

          {props.uploadInfoError && (
            <div className="upload-info-error">
              You must give your exhibition a title, a description and choose a
              poster.
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
              placeholder="Describe your exhibition"
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
              Collaborators
            </label>
            <Select
              className="mt-1"
              placeholder="Add collaborators"
              options={props.users}
              maxMenuHeight={170}
              isMulti
              styles={{
                control: (baseStyles) => ({
                  ...baseStyles,
                  fontSize: "14px",
                  borderRadius: "6px",
                  borderColor: "#18121c",
                  boxShadow: "none",
                  outline: "none",
                }),
                menu: (baseStyles) => ({
                  ...baseStyles,
                  fontSize: "14px",
                  color: "#000000",
                }),
                option: (baseStyles) => ({
                  ...baseStyles,
                  paddingTop: "3px",
                  paddingBottom: "3px",
                }),
              }}
              value={collaborators}
              onChange={handleCollaborators}
            />
          </div>

          <div className="form-group mt-3">
            <label className="access-label" style={{ color: "#ffc9ff" }}>
              Start date
            </label>
            <DatePicker
              className="form-control mt-1"
              dateFormat="dd/MM/yyyy"
              selected={startDate}
              onChange={(date) => setStartDate(date)}
            />
          </div>

          <div className="form-group mt-3">
            <label className="access-label" style={{ color: "#ffc9ff" }}>
              End date
            </label>
            <DatePicker
              className="form-control mt-1"
              dateFormat="dd/MM/yyyy"
              selected={endDate}
              onChange={(date) => setEndDate(date)}
            />
          </div>
          <div className="d-grid gap-2 mt-4">
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

export default UploadOnlineExhibitionCard;
