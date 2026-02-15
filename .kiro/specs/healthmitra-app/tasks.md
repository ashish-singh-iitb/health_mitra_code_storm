# Implementation Plan: HealthMitra App

## Overview

This implementation plan breaks down the HealthMitra WhatsApp-based healthcare assistant into discrete coding tasks. The system will be built using Python with a modular architecture separating communication, processing, data, and orchestration layers. Each task builds incrementally, with property-based tests using Hypothesis to validate correctness properties from the design document.

## Tasks

- [ ] 1. Set up project structure and core infrastructure
  - Create Python project with virtual environment
  - Set up directory structure: `src/`, `tests/`, `config/`
  - Install core dependencies: FastAPI, SQLAlchemy, Redis, Hypothesis, pytest
  - Create configuration management for environment variables
  - Set up logging infrastructure
  - _Requirements: All (foundational)_

- [ ] 2. Implement data models and database layer
  - [ ] 2.1 Create database schema and models
    - Define SQLAlchemy models for: PatientProfile, SymptomRecord, MedicationPlan, AdherenceLog, RecoveryCheck, Journey
    - Implement encryption for sensitive health data fields
    - Create database migration scripts using Alembic
    - _Requirements: 11.1, 11.5_
  
  - [ ]* 2.2 Write property test for patient data encryption
    - **Property 50: Health Data Encryption at Rest**
    - **Validates: Requirements 11.1**
  
  - [ ]* 2.3 Write property test for patient data association
    - **Property 51: Patient Data Association**
    - **Validates: Requirements 11.5**
  
  - [ ] 2.4 Implement PatientProfileRepository
    - Create CRUD operations for patient profiles
    - Implement symptom history and classification history storage
    - Implement secure data deletion
    - _Requirements: 11.5, 11.6_
  
  - [ ]* 2.5 Write property test for data deletion completeness
    - **Property 52: Complete Data Deletion**
    - **Validates: Requirements 11.6**

- [ ] 3. Implement Language Manager component
  - [ ] 3.1 Create LanguageManager class
    - Implement language detection using langdetect library
    - Implement language preference storage and retrieval
    - Integrate with Google Cloud Translation API
    - Implement structured content translation
    - _Requirements: 1.2, 1.3, 1.4, 1.5_
  
  - [ ]* 3.2 Write property test for language preference persistence
    - **Property 1: Language Preference Persistence**
    - **Validates: Requirements 1.2**
  
  - [ ]* 3.3 Write property test for language detection
    - **Property 2: Language Detection Accuracy**
    - **Validates: Requirements 1.3**
  
  - [ ]* 3.4 Write property test for universal language application
    - **Property 3: Universal Language Preference Application**
    - **Validates: Requirements 1.4, 3.3, 4.7, 5.6, 7.4, 8.2, 8.8, 9.6**
  
  - [ ]* 3.5 Write property test for language preference updates
    - **Property 4: Language Preference Update**
    - **Validates: Requirements 1.5**

- [ ] 4. Implement WhatsApp Interface and Message Handler
  - [ ] 4.1 Create WhatsAppInterface class
    - Integrate with WhatsApp Business API using whatsapp-python library
    - Implement webhook handler for incoming messages
    - Implement message sending with retry logic
    - Implement media download functionality
    - _Requirements: 10.1, 10.2, 10.3, 10.5_
  
  - [ ] 4.2 Create MessageHandler class
    - Implement message parsing and intent detection
    - Implement message routing logic
    - Implement message validation
    - _Requirements: 10.4, 10.6_
  
  - [ ]* 4.3 Write property test for WhatsApp message formatting
    - **Property 46: WhatsApp Message Formatting**
    - **Validates: Requirements 10.4**
  
  - [ ]* 4.4 Write property test for multimedia content processing
    - **Property 47: Multimedia Content Processing**
    - **Validates: Requirements 10.5**
  
  - [ ]* 4.5 Write property test for structured information formatting
    - **Property 48: Structured Information Formatting**
    - **Validates: Requirements 10.6**
  
  - [ ]* 4.6 Write property test for failed delivery retry
    - **Property 49: Failed Delivery Retry**
    - **Validates: Requirements 10.7**

- [ ] 5. Checkpoint - Ensure infrastructure tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 6. Implement Symptom Interpreter component
  - [ ] 6.1 Create SymptomInterpreter class
    - Integrate Google Cloud Speech-to-Text for voice processing
    - Implement text symptom extraction using NLP (spaCy)
    - Implement symptom normalization to medical terms
    - Implement visual symptom processing (basic image analysis)
    - Calculate confidence scores for extractions
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5_
  
  - [ ]* 6.2 Write property test for text symptom extraction
    - **Property 5: Text Symptom Extraction Completeness**
    - **Validates: Requirements 2.1, 2.5**
  
  - [ ]* 6.3 Write property test for voice symptom processing
    - **Property 6: Voice Symptom Processing Pipeline**
    - **Validates: Requirements 2.2**
  
  - [ ]* 6.4 Write property test for visual input processing
    - **Property 7: Visual Input Processing**
    - **Validates: Requirements 2.3**
  
  - [ ]* 6.5 Write property test for symptom normalization
    - **Property 8: Symptom Normalization**
    - **Validates: Requirements 2.4**
  
  - [ ]* 6.6 Write property test for low confidence clarification
    - **Property 9: Low Confidence Clarification**
    - **Validates: Requirements 2.6, 12.5**
  
  - [ ]* 6.7 Write property test for informal text handling
    - **Property 53: Informal Text Handling**
    - **Validates: Requirements 12.3**
  
  - [ ]* 6.8 Write property test for context preservation
    - **Property 54: Context Preservation in Extraction**
    - **Validates: Requirements 12.4**

- [ ] 7. Implement Severity Classifier component
  - [ ] 7.1 Create SeverityClassifier class
    - Define medical safety rules for severity classification
    - Implement severity level assignment (S1-S5)
    - Implement safety assessment with red flags
    - Generate classification reasons and recommendations
    - Include safety disclaimers in all outputs
    - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5_
  
  - [ ]* 7.2 Write property test for classification triggering
    - **Property 10: Classification Triggering**
    - **Validates: Requirements 3.1**
  
  - [ ]* 7.3 Write property test for valid severity levels
    - **Property 11: Valid Severity Level Assignment**
    - **Validates: Requirements 3.2**
  
  - [ ]* 7.4 Write property test for classification completeness
    - **Property 12: Classification Completeness**
    - **Validates: Requirements 3.3, 3.4, 3.5**
  
  - [ ]* 7.5 Write unit test for emergency condition classification
    - Test that specific emergency symptoms (chest pain, difficulty breathing) classify as S1
    - _Requirements: 3.6_
  
  - [ ]* 7.6 Write property test for consistent reclassification rules
    - **Property 13: Consistent Reclassification Rules**
    - **Validates: Requirements 9.2**

- [ ] 8. Implement Care Navigator component
  - [ ] 8.1 Create CareNavigator class
    - Integrate with Google Maps API for facility search
    - Implement facility filtering by type and severity
    - Implement distance-based sorting
    - Generate care guidance based on severity
    - Generate home care advice for mild cases
    - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6_
  
  - [ ]* 8.2 Write property test for emergency facility recommendations
    - **Property 14: Emergency Care Facility Recommendations**
    - **Validates: Requirements 4.1**
  
  - [ ]* 8.3 Write property test for moderate care recommendations
    - **Property 15: Moderate Care Facility Recommendations**
    - **Validates: Requirements 4.2**
  
  - [ ]* 8.4 Write property test for pharmacy recommendations
    - **Property 16: Pharmacy Recommendations for Medication**
    - **Validates: Requirements 4.3**
  
  - [ ]* 8.5 Write property test for location-based sorting
    - **Property 17: Location-Based Facility Sorting**
    - **Validates: Requirements 4.4**
  
  - [ ]* 8.6 Write property test for home care guidance
    - **Property 18: Home Care Guidance for Mild Cases**
    - **Validates: Requirements 4.5**
  
  - [ ]* 8.7 Write property test for care navigation completeness
    - **Property 19: Care Navigation Completeness**
    - **Validates: Requirements 4.6**

- [ ] 9. Checkpoint - Ensure symptom and classification tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 10. Implement Content Extractor component
  - [ ] 10.1 Create ContentExtractor class
    - Integrate Google Cloud Vision API for OCR
    - Implement prescription data extraction from images
    - Implement consultation audio transcription
    - Parse medical content to extract structured information
    - Generate consultation summaries
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5_
  
  - [ ]* 10.2 Write property test for prescription OCR
    - **Property 20: Prescription OCR Processing**
    - **Validates: Requirements 5.1**
  
  - [ ]* 10.3 Write property test for audio transcription
    - **Property 21: Consultation Audio Transcription**
    - **Validates: Requirements 5.2**
  
  - [ ]* 10.4 Write property test for medical information extraction
    - **Property 22: Medical Information Extraction**
    - **Validates: Requirements 5.3**
  
  - [ ]* 10.5 Write property test for summary generation
    - **Property 23: Consultation Summary Generation**
    - **Validates: Requirements 5.4**
  
  - [ ]* 10.6 Write property test for summary completeness
    - **Property 24: Consultation Summary Completeness**
    - **Validates: Requirements 5.5**
  
  - [ ]* 10.7 Write property test for low quality clarification
    - **Property 25: Low Quality Extraction Clarification**
    - **Validates: Requirements 5.7**

- [ ] 11. Implement Medication Plan Manager component
  - [ ] 11.1 Create MedicationPlanManager class
    - Implement medication plan creation from prescriptions
    - Implement plan storage and retrieval
    - Implement medication schedule organization
    - Implement plan validation
    - Implement adherence recording
    - Calculate adherence statistics
    - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.5, 6.6_
  
  - [ ]* 11.2 Write property test for plan creation
    - **Property 26: Medication Plan Creation**
    - **Validates: Requirements 6.1**
  
  - [ ]* 11.3 Write property test for plan data completeness
    - **Property 27: Medication Plan Data Completeness**
    - **Validates: Requirements 6.2**
  
  - [ ]* 11.4 Write property test for multi-medication organization
    - **Property 28: Multi-Medication Organization**
    - **Validates: Requirements 6.3**
  
  - [ ]* 11.5 Write property test for plan validation
    - **Property 29: Medication Plan Validation**
    - **Validates: Requirements 6.4**
  
  - [ ]* 11.6 Write property test for incomplete prescription handling
    - **Property 30: Incomplete Prescription Handling**
    - **Validates: Requirements 6.5**
  
  - [ ]* 11.7 Write property test for plan persistence
    - **Property 31: Medication Plan Persistence**
    - **Validates: Requirements 6.6**

- [ ] 12. Implement Reminder Generator component
  - [ ] 12.1 Create ReminderGenerator class
    - Implement reminder scheduling using Bull queue
    - Generate reminder messages with medication details
    - Implement reminder delivery via WhatsApp
    - Implement missed reminder follow-up logic
    - Implement reminder cancellation
    - _Requirements: 7.1, 7.2, 7.3, 7.5, 7.6, 7.7_
  
  - [ ]* 12.2 Write property test for reminder generation
    - **Property 32: Reminder Generation from Plan**
    - **Validates: Requirements 7.1**
  
  - [ ]* 12.3 Write property test for reminder delivery
    - **Property 33: Reminder Delivery at Scheduled Time**
    - **Validates: Requirements 7.2**
  
  - [ ]* 12.4 Write property test for reminder content
    - **Property 34: Reminder Content Completeness**
    - **Validates: Requirements 7.3**
  
  - [ ]* 12.5 Write property test for missed reminder follow-up
    - **Property 35: Missed Reminder Follow-up**
    - **Validates: Requirements 7.5**
  
  - [ ]* 12.6 Write property test for reminder expiration
    - **Property 36: Reminder Expiration**
    - **Validates: Requirements 7.6**
  
  - [ ]* 12.7 Write property test for plan completion notification
    - **Property 37: Plan Completion Notification**
    - **Validates: Requirements 7.7**

- [ ] 13. Checkpoint - Ensure consultation and medication tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 14. Implement Recovery Monitor component
  - [ ] 14.1 Create RecoveryMonitor class
    - Implement check-in scheduling using Bull queue
    - Generate check-in messages in patient's language
    - Process check-in responses (text, voice, image)
    - Analyze recovery trends and determine status
    - Implement reclassification triggering logic
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5, 8.6_
  
  - [ ]* 14.2 Write property test for check-in scheduling
    - **Property 38: Periodic Check-in Scheduling**
    - **Validates: Requirements 8.1**
  
  - [ ]* 14.3 Write property test for multi-modal response handling
    - **Property 39: Multi-modal Check-in Response Handling**
    - **Validates: Requirements 8.3**
  
  - [ ]* 14.4 Write property test for recovery status determination
    - **Property 40: Recovery Status Determination**
    - **Validates: Requirements 8.4, 8.5**
  
  - [ ]* 14.5 Write property test for worsening reclassification
    - **Property 41: Worsening Condition Reclassification**
    - **Validates: Requirements 8.6, 9.1, 13.6**
  
  - [ ]* 14.6 Write property test for reclassification care updates
    - **Property 42: Reclassification Care Updates**
    - **Validates: Requirements 8.7**
  
  - [ ]* 14.7 Write property test for severity comparison
    - **Property 43: Severity Level Comparison**
    - **Validates: Requirements 9.3**
  
  - [ ]* 14.8 Write property test for escalated care
    - **Property 44: Escalated Care for Severity Increase**
    - **Validates: Requirements 9.4**
  
  - [ ]* 14.9 Write property test for continued recovery guidance
    - **Property 45: Continued Recovery Guidance for Severity Decrease**
    - **Validates: Requirements 9.5**
  
  - [ ]* 14.10 Write unit test for emergency escalation during monitoring
    - Test that worsening to S1/S2 during monitoring triggers immediate emergency guidance
    - _Requirements: 9.7_

- [ ] 15. Implement Journey Manager and Workflow Coordinator
  - [ ] 15.1 Create JourneyManager class
    - Implement journey initialization for new patients
    - Implement journey state management
    - Implement step progression logic
    - Implement step completion tracking
    - Implement journey reset for reclassification
    - _Requirements: 13.1, 13.2, 13.3, 13.4, 13.5, 13.7_
  
  - [ ] 15.2 Create WorkflowCoordinator class
    - Orchestrate component interactions
    - Implement automatic step transitions
    - Handle workflow errors and retries
    - Maintain conversation context
    - _Requirements: 13.1, 13.2, 13.3, 13.4, 13.5_
  
  - [ ]* 15.3 Write property test for symptom to classification progression
    - **Property 56: Symptom to Classification Progression**
    - **Validates: Requirements 13.1**
  
  - [ ]* 15.4 Write property test for classification to navigation progression
    - **Property 57: Classification to Navigation Progression**
    - **Validates: Requirements 13.2**
  
  - [ ]* 15.5 Write property test for consultation to summary progression
    - **Property 58: Consultation to Summary Progression**
    - **Validates: Requirements 13.3**
  
  - [ ]* 15.6 Write property test for plan to reminders progression
    - **Property 59: Plan to Reminders Progression**
    - **Validates: Requirements 13.4**
  
  - [ ]* 15.7 Write property test for reminders to monitoring progression
    - **Property 60: Reminders to Monitoring Progression**
    - **Validates: Requirements 13.5**
  
  - [ ]* 15.8 Write property test for journey state persistence
    - **Property 61: Journey State Persistence**
    - **Validates: Requirements 13.7**

- [ ] 16. Implement error handling and processing error messages
  - [ ] 16.1 Create error handling middleware
    - Implement graceful degradation strategies
    - Implement retry logic for external services
    - Implement error logging and monitoring
    - Generate user-friendly error messages
    - _Requirements: 12.7_
  
  - [ ]* 16.2 Write property test for processing error messages
    - **Property 55: Processing Error Messages**
    - **Validates: Requirements 12.7**

- [ ] 17. Implement API endpoints and request handlers
  - [ ] 17.1 Create FastAPI application
    - Implement webhook endpoint for WhatsApp messages
    - Implement health check endpoint
    - Implement admin endpoints for monitoring
    - Add request validation and authentication
    - _Requirements: 10.1, 10.2_
  
  - [ ] 17.2 Implement background job workers
    - Set up Bull queue workers for reminders
    - Set up Bull queue workers for check-ins
    - Set up Bull queue workers for message retries
    - _Requirements: 7.2, 8.1, 10.7_

- [ ] 18. Checkpoint - Ensure workflow and integration tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 19. Implement initial patient onboarding flow
  - [ ] 19.1 Create onboarding handler
    - Detect first-time patients
    - Send language selection prompt
    - Handle language selection response
    - Initialize patient profile and journey
    - _Requirements: 1.1, 1.2_
  
  - [ ]* 19.2 Write unit test for first-time interaction
    - Test that new patients receive language selection prompt
    - _Requirements: 1.1_

- [ ] 20. Create configuration and deployment files
  - [ ] 20.1 Create configuration files
    - Create `.env.example` with all required environment variables
    - Create `requirements.txt` with all Python dependencies
    - Create `docker-compose.yml` for local development
    - Create Dockerfile for containerization
    - _Requirements: All (deployment)_
  
  - [ ] 20.2 Create documentation
    - Create README.md with setup instructions
    - Create API documentation
    - Create deployment guide
    - Document environment variables and configuration
    - _Requirements: All (documentation)_

- [ ] 21. Final integration testing and validation
  - [ ]* 21.1 Write integration tests for complete journey flows
    - Test complete 6-step journey from symptom to recovery
    - Test journey interruption and resumption
    - Test concurrent patient journeys
    - _Requirements: 13.7_
  
  - [ ]* 21.2 Write integration tests for external services
    - Test WhatsApp API integration with mocks
    - Test translation service with fallbacks
    - Test OCR service with various image qualities
    - Test location service with different regions
    - _Requirements: 10.1, 10.5, 5.1, 4.4_

- [ ] 22. Final checkpoint - Ensure all tests pass
  - Run complete test suite
  - Verify all property tests pass with 100+ iterations
  - Verify all unit tests pass
  - Verify all integration tests pass
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each property test should run minimum 100 iterations using Hypothesis
- Property tests should be tagged with: `# Feature: healthmitra-app, Property {number}: {property_text}`
- Use mocks for external services (WhatsApp, Google Cloud APIs) during testing
- Implement comprehensive logging for debugging and monitoring
- Follow Python best practices: type hints, docstrings, PEP 8 style guide
- Use environment variables for all sensitive configuration (API keys, database URLs)
- Checkpoints ensure incremental validation and provide opportunities for user feedback
