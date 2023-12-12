import {
  Container,
  SimpleGrid,
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalCloseButton,
  ModalBody,
  ModalFooter,
  Button,
} from "@chakra-ui/react";
import axios from "axios";
import { nanoid } from "nanoid";
import { faker } from "@faker-js/faker";
import React, { useEffect, useState } from "react";
import Result from "../components/Result";
import SearchBar from "../components/SearchBar";

export default function Search() {
  const [query, setQuery] = useState("");
  const [projects, setProjects] = useState([]);
  const [selectedProject, setSelectedProject] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

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
  };

  const handleCloseModal = () => {
    setSelectedProject(null);
    setIsModalOpen(false);
  };

  return (
    <Container maxW="container.lg" py="8">
      <SearchBar onSearch={handleSearch} />
      <SimpleGrid columns={[1, 2, 3, 4]} spacing="4">
        {searchedProjects.map((project) => (
          <Result
            key={nanoid()}
            data={project}
            onOpenClick={() => handleOpenClick(project.id)}
          />
        ))}
      </SimpleGrid>
      <Modal isOpen={isModalOpen} onClose={handleCloseModal} size="3xl">
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>{selectedProject?.title}</ModalHeader>
          <ModalCloseButton />
          <ModalBody>
            <p>Date: {selectedProject?.date}</p>
            {selectedProject?.googleDriveLink && (
              <iframe
                title="Google Drive File"
                src={selectedProject.googleDriveLink}
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
