import React, { useState } from "react";

import "./styles/ArtItemSelection.css";

function ArtItemSelection(props) {
  const [selectedArtItemIndexes, setSelectedArtItemIndexes] = useState(
    props.artItemsGalleryIndexes
  );

  //console.log(selectedArtItemIndexes);

  const [selectedArtItems, setSelectedArtItems] = useState(
    props.artItemsGallery
  );

  //console.log(selectedArtItems);

  function handleClick(id, index) {
    const copy = [...selectedArtItemIndexes];
    copy[index] = !selectedArtItemIndexes[index];
    setSelectedArtItemIndexes(copy);

    if (copy[index]) {
      setSelectedArtItems((current) => [...current, id]);
    } else {
      setSelectedArtItems((current) =>
        current.filter((currentElement) => currentElement !== id)
      );
    }
  }

  // console.log("Indexes: " + selectedArtItemIndexes);
  // console.log("IDs: " + selectedArtItems);

  return (
    <div className="artitem-selection-container">
      <header className="artitem-selection-header">
        Click on the art items that you want to add to your exhibition
      </header>
      <main>
        <div className="gallery">
          {props.userGallery.map((val, index) => {
            return (
              <div key={val.id} className="gallery-item">
                <img
                  src={val.artitem_path}
                  className="gallery-image"
                  alt={val.description}
                />
                <div
                  className="gallery-image-options-container"
                  style={
                    selectedArtItemIndexes[index]
                      ? {
                          display: "flex",
                          justifyContent: "center",
                          alignItems: "center",
                          position: "absolute",
                          top: "0",
                          width: "100%",
                          height: "100%",
                          backgroundColor: "rgba(200, 200, 200, 0.8)",
                        }
                      : { display: "flex" }
                  }
                  onClick={() => handleClick(val.id, index)}
                ></div>
              </div>
            );
          })}
        </div>
        <div className="artitem-selection-buttons">
          <button
            onClick={props.onClickCancel}
            className="btn btn-secondary artitem-selection-btn"
          >
            Cancel
          </button>
          <button
            onClick={() =>
              props.onClickAdd(selectedArtItems, selectedArtItemIndexes)
            }
            className="btn btn-primary artitem-selection-btn"
          >
            Add
          </button>
        </div>
      </main>
    </div>
  );
}

export default ArtItemSelection;
