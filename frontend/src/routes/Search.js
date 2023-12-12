import { Container, SimpleGrid } from "@chakra-ui/react";
import axios from "axios";
import { nanoid } from "nanoid";
import { faker } from "@faker-js/faker";
import React, { useEffect, useState } from "react";
import Result from "../components/Result";
import SearchBar from "../components/SearchBar";

const handleOpenClick = () => {
  console.log("Open button clicked!");
};

export default function Search() {
  const [query, setQuery] = useState("");
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/authors/")
      .then((response) => {
        const data = response.data;
        data.forEach((project) => {
          project.imageUrl = "https://placekitten.com/300/200";
          project.date = faker.date.past().toLocaleDateString();
          project.extension = faker.system.commonFileExt();
        });
        setProjects(data);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  // Filter projects based on the search query
  const searchedProjecs = projects.filter(
    (project) =>
      project.name.toLowerCase().includes(query.toLowerCase()) ||
      project.extension === query.toLowerCase()
  );

  const handleSearch = (searchQuery) => {
    setQuery(searchQuery);
  };

  return (
    <Container maxW="container.lg" py="8">
      <SearchBar onSearch={handleSearch} />
      <SimpleGrid columns={[1, 2, 3, 4]} spacing="4">
        {searchedProjecs.map((project) => (
          <Result
            key={nanoid()}
            data={project}
            onOpenClick={() => handleOpenClick(project.id)}
          />
        ))}
      </SimpleGrid>
    </Container>
  );
}
