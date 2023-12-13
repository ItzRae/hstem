import {
  Container,
  Flex,
  SimpleGrid,
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalCloseButton,
  ModalBody,
  ModalFooter,
  Button,
  Text,
  Box
} from "@chakra-ui/react";
import axios from "axios";
import { nanoid } from "nanoid";
import { faker } from "@faker-js/faker";
import React, { useEffect, useState } from "react";
import Result from "../components/Result";
import SearchBar from "../components/SearchBar";

function isValidURL(str) {
  try {
    new URL(str);
    return true;
  } catch (error) {
    return false;
  }
}

export default function Search() {
  const [query, setQuery] = useState("");
  const [projects, setProjects] = useState([]);
  const [selectedProject, setSelectedProject] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [authorDetails, setAuthorDetails] = useState(null);
  const [previewUrl, setPreviewUrl] = useState("");

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/projects/")
      .then((response) => {
        const data = response.data;
        data.forEach((project) => {
          project.id = nanoid();
          project.imageUrl = "https://placekitten.com/300/200";
          project.date = faker.date.past().toLocaleDateString();
        });
        setProjects(data);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  // Filter projects based on the search query
  const searchedProjects = projects.filter((project) =>
    project.title.toLowerCase().includes(query.toLowerCase())
  );

  const handleSearch = (searchQuery) => {
    setQuery(searchQuery);
  };

  const handleOpenClick = (projectId) => {
    const project = projects.find((project) => project.id === projectId);
    setSelectedProject(project);
    setIsModalOpen(true);

    // Fetch additional details based on the selected project's title
    const encodedTitle = encodeURIComponent(project.title);
    axios
      .get(`http://localhost:8000/api/details/${encodedTitle}/`)
      .then((response) => {
        console.log(response.data);
        const { creates: { author }, file } = response.data;
        setAuthorDetails(author);
        setPreviewUrl(file.file);
      })
      .catch((error) => {
        console.error("Error fetching author details:", error);
      });
  };

  const handleCloseModal = () => {
    setSelectedProject(null);
    setIsModalOpen(false);
  };

  return (
    <Container maxW="container.lg" py="8">
      <Flex flexWrap="wrap">
        <Box w={{ base: "100%", md: "20%" }} pr={{ base: "0", md: "4" }}>
          <SearchBar onSearch={handleSearch} />
        </Box>
        <Box w={{ base: "100%", md: "80%" }}>
          <SimpleGrid columns={[1, 2, 3, 4]} spacing="4">
            {searchedProjects.map((project) => (
              <Result
                key={nanoid()}
                data={project}
                onOpenClick={() => handleOpenClick(project.id)}
              />
            ))}
          </SimpleGrid>
        </Box>
      </Flex>
      <Modal isOpen={isModalOpen} onClose={handleCloseModal} size="3xl">
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>{selectedProject?.title}</ModalHeader>
          <ModalCloseButton />
          <ModalBody>
            <Text>Date: {selectedProject?.date}</Text>
            <Text>Author: {authorDetails?.name}</Text>
            <Text>Major(s): {authorDetails?.major}</Text>
            <Text>Year: {authorDetails?.year}</Text>
            {previewUrl && isValidURL(previewUrl) && (
              <iframe
                title="Google Drive File"
                src={previewUrl}
                width="100%"
                height="500px"
              />
            )}
          </ModalBody>
          <ModalFooter>
            <Button colorScheme="purple" mr={3} onClick={handleCloseModal}>
              Close
            </Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </Container>
  );
}