# Requirements Document

## Introduction

HealthMitra is a WhatsApp-based multilingual healthcare assistant that guides patients through a complete 6-step healthcare journey, from initial symptom input through recovery monitoring. The system provides intelligent symptom analysis, severity classification, care navigation, consultation recording, medication tracking, and continuous recovery monitoring, all delivered in the patient's preferred language.

## Glossary

- **System**: The HealthMitra healthcare assistant application
- **Patient**: The end user interacting with the system via WhatsApp
- **Symptom_Profile**: A structured representation of patient symptoms including main symptoms, triggers, context, and risk indicators
- **Severity_Level**: A classification from S1 (Emergency) to S5 (Wellness) indicating urgency of care needed
- **Care_Option**: A recommended healthcare facility or action (hospital, clinic, pharmacy, home care)
- **Consultation_Summary**: A structured patient-friendly summary of doctor's diagnosis, medications, and instructions
- **Medication_Plan**: A structured schedule of medicines with dosage, timing, and duration
- **Recovery_Status**: An assessment of patient progress (improving, unchanged, worsening)
- **Language_Preference**: The patient's chosen language for all system interactions
- **WhatsApp_Interface**: The messaging platform through which all patient interactions occur

## Requirements

### Requirement 1: Language Selection and Preference Management

**User Story:** As a patient, I want to interact with the system in my preferred language, so that I can understand all health information and communicate my symptoms effectively.

#### Acceptance Criteria

1. WHEN a patient first interacts with the System, THE System SHALL prompt the patient to select their preferred language
2. WHEN a patient selects a language, THE System SHALL store the Language_Preference for all future interactions
3. WHEN a patient provides input in any language, THE System SHALL detect the input language automatically
4. WHERE a patient has set a Language_Preference, THE System SHALL deliver all responses in that language
5. WHEN a patient requests to change their language, THE System SHALL update the Language_Preference and use the new language for subsequent interactions

### Requirement 2: Symptom Input and Processing

**User Story:** As a patient, I want to describe my symptoms using text, voice, or images, so that the system can understand my health concern without requiring technical medical knowledge.

#### Acceptance Criteria

1. WHEN a patient sends a text message describing symptoms, THE System SHALL extract key symptoms and relevant context
2. WHEN a patient sends a voice message, THE System SHALL convert the audio to text and extract symptoms
3. WHEN a patient sends a photo or video, THE System SHALL process the visual input and extract relevant health information
4. WHEN symptom input is received, THE System SHALL normalize the symptoms into structured medical terms
5. WHEN symptom extraction is complete, THE System SHALL create a Symptom_Profile containing main symptoms, triggers, context, and risk indicators
6. IF symptom input is unclear or insufficient, THEN THE System SHALL ask clarifying questions in the patient's Language_Preference

### Requirement 3: Severity Classification

**User Story:** As a patient, I want the system to assess how serious my condition is, so that I know what level of care I need and how urgently.

#### Acceptance Criteria

1. WHEN a Symptom_Profile is created, THE System SHALL analyze the symptoms using medical safety rules
2. WHEN severity analysis is complete, THE System SHALL assign one of five Severity_Levels: S1 (Emergency), S2 (Urgent), S3 (Moderate), S4 (Mild), or S5 (Wellness)
3. WHEN a Severity_Level is assigned, THE System SHALL provide a clear reason for the classification in the patient's Language_Preference
4. WHEN a Severity_Level is assigned, THE System SHALL recommend the appropriate next action
5. WHEN providing severity information, THE System SHALL include a safety disclaimer stating that this is guidance and not a medical diagnosis
6. IF symptoms indicate emergency conditions, THEN THE System SHALL classify as S1 and recommend immediate hospital care
7. WHEN severity classification is complete, THE System SHALL deliver all information in the patient's Language_Preference

### Requirement 4: Care Navigation and Facility Recommendations

**User Story:** As a patient, I want to receive recommendations for nearby healthcare facilities appropriate to my condition severity, so that I can access the right care quickly.

#### Acceptance Criteria

1. WHEN a Severity_Level is S1 or S2, THE System SHALL provide a list of nearest hospitals with contact information
2. WHEN a Severity_Level is S3, THE System SHALL provide a list of nearby clinics
3. WHEN any Severity_Level requires medication, THE System SHALL provide locations of nearby medicine stores
4. WHEN providing facility recommendations, THE System SHALL use the patient's location data to find nearby options
5. WHEN a Severity_Level is S4 or S5, THE System SHALL provide home care advice and precautionary steps
6. WHEN providing care navigation, THE System SHALL include clear instructions on what to do, what to avoid, and when to seek professional care
7. WHEN delivering care navigation information, THE System SHALL present all content in the patient's Language_Preference

### Requirement 5: Consultation Recording and Summary Generation

**User Story:** As a patient, I want to upload my prescription and consultation notes, so that the system can help me understand and remember the doctor's instructions.

#### Acceptance Criteria

1. WHEN a patient uploads a prescription photo, THE System SHALL perform OCR to extract text from the image
2. WHEN a patient sends consultation audio, THE System SHALL transcribe the audio to text
3. WHEN prescription or consultation data is received, THE System SHALL extract diagnosis information, medicine names, dosage, timing, duration, and doctor's advice
4. WHEN extraction is complete, THE System SHALL generate a Consultation_Summary in a simple, structured format
5. WHEN creating a Consultation_Summary, THE System SHALL include condition overview, medication schedule, key instructions, and diet or activity advice
6. WHEN a Consultation_Summary is generated, THE System SHALL deliver it in the patient's Language_Preference
7. IF OCR or transcription quality is poor, THEN THE System SHALL request clarification from the patient

### Requirement 6: Medication Plan Creation and Storage

**User Story:** As a patient, I want the system to create a medication schedule from my prescription, so that I know exactly when and how to take each medicine.

#### Acceptance Criteria

1. WHEN a prescription is processed, THE System SHALL create a structured Medication_Plan
2. WHEN creating a Medication_Plan, THE System SHALL store medicine names, dosage amounts, timing schedules, and treatment duration
3. WHEN a Medication_Plan includes multiple medicines, THE System SHALL organize them by timing to avoid confusion
4. WHEN a Medication_Plan is created, THE System SHALL validate that all required information (medicine, dosage, timing, duration) is present
5. IF prescription information is incomplete, THEN THE System SHALL request missing details from the patient
6. WHEN a Medication_Plan is stored, THE System SHALL make it accessible for reminder generation and tracking

### Requirement 7: Medication Reminders and Adherence Tracking

**User Story:** As a patient, I want to receive timely reminders to take my medications, so that I follow my treatment plan correctly.

#### Acceptance Criteria

1. WHEN a Medication_Plan exists, THE System SHALL generate reminder messages for each scheduled medication time
2. WHEN a medication reminder time arrives, THE System SHALL send a WhatsApp_Interface message to the patient
3. WHEN sending a reminder, THE System SHALL include the medicine name, dosage, and any special instructions
4. WHEN a reminder is sent, THE System SHALL deliver it in the patient's Language_Preference
5. WHEN a patient does not acknowledge a reminder within a reasonable time, THE System SHALL send a follow-up prompt
6. WHEN the medication duration expires, THE System SHALL stop sending reminders for that medicine
7. WHEN all medications in a Medication_Plan are completed, THE System SHALL notify the patient and suggest a recovery check-in

### Requirement 8: Recovery Monitoring and Check-ins

**User Story:** As a patient, I want the system to check on my recovery progress, so that I can get updated guidance if my condition changes.

#### Acceptance Criteria

1. WHEN a patient is following a treatment plan, THE System SHALL periodically send check-in messages asking about recovery progress
2. WHEN sending check-in messages, THE System SHALL ask simple recovery-related questions in the patient's Language_Preference
3. WHEN a patient responds to a check-in, THE System SHALL accept text, voice, or image responses
4. WHEN analyzing check-in responses, THE System SHALL determine if the condition is improving, unchanged, or worsening
5. WHEN recovery analysis is complete, THE System SHALL generate a Recovery_Status assessment
6. WHEN a Recovery_Status indicates worsening, THE System SHALL reclassify the Severity_Level
7. WHEN reclassification occurs, THE System SHALL provide updated care recommendations based on the new Severity_Level
8. WHEN recovery monitoring results are delivered, THE System SHALL present all information in the patient's Language_Preference

### Requirement 9: Severity Reclassification and Adaptive Guidance

**User Story:** As a patient, I want the system to adjust its recommendations if my condition changes, so that I always receive appropriate guidance for my current health status.

#### Acceptance Criteria

1. WHEN a Recovery_Status indicates significant change, THE System SHALL perform severity reclassification
2. WHEN reclassifying severity, THE System SHALL use the same medical safety rules as initial classification
3. WHEN a new Severity_Level is assigned during recovery monitoring, THE System SHALL compare it to the previous level
4. IF the new Severity_Level is higher than the previous level, THEN THE System SHALL recommend escalated care options
5. IF the new Severity_Level is lower than the previous level, THEN THE System SHALL provide updated guidance for continued recovery
6. WHEN reclassification is complete, THE System SHALL deliver the updated assessment and recommendations in the patient's Language_Preference
7. WHEN severity increases to S1 or S2 during monitoring, THE System SHALL immediately provide emergency or urgent care guidance

### Requirement 10: WhatsApp Integration and Message Handling

**User Story:** As a patient, I want to interact with the system entirely through WhatsApp, so that I don't need to install additional apps or learn new interfaces.

#### Acceptance Criteria

1. THE System SHALL integrate with the WhatsApp_Interface to send and receive messages
2. WHEN a patient sends a message via WhatsApp, THE System SHALL receive and process it within a reasonable time
3. WHEN the System generates a response, THE System SHALL deliver it via the WhatsApp_Interface
4. WHEN sending messages, THE System SHALL format them appropriately for WhatsApp display
5. WHEN a patient sends multimedia content (voice, image, video), THE System SHALL download and process the content
6. WHEN the System needs to send structured information, THE System SHALL format it clearly using WhatsApp message formatting capabilities
7. IF WhatsApp_Interface connectivity fails, THEN THE System SHALL queue messages and retry delivery

### Requirement 11: Data Privacy and Security

**User Story:** As a patient, I want my health information to be kept private and secure, so that I can trust the system with sensitive medical data.

#### Acceptance Criteria

1. WHEN the System stores patient data, THE System SHALL encrypt all health information at rest
2. WHEN the System transmits patient data, THE System SHALL use secure encrypted connections
3. WHEN a patient's session ends, THE System SHALL maintain data privacy by not sharing information with unauthorized parties
4. THE System SHALL comply with applicable healthcare data protection regulations
5. WHEN storing Symptom_Profiles, Consultation_Summaries, or Medication_Plans, THE System SHALL associate them only with the authenticated patient
6. WHEN a patient requests data deletion, THE System SHALL remove all stored personal health information
7. THE System SHALL not use patient health data for purposes other than providing healthcare guidance without explicit consent

### Requirement 12: Multi-modal Input Processing

**User Story:** As a patient, I want the system to accurately process different types of input (text, voice, images), so that I can communicate in the way that's most convenient for me.

#### Acceptance Criteria

1. WHEN processing voice input, THE System SHALL use speech-to-text conversion with accuracy appropriate for medical terminology
2. WHEN processing image input, THE System SHALL use OCR with accuracy sufficient to read prescriptions and medical documents
3. WHEN processing text input, THE System SHALL handle informal language, typos, and colloquialisms
4. WHEN processing any input type, THE System SHALL extract medical information while preserving context
5. IF input processing confidence is low, THEN THE System SHALL ask the patient for clarification
6. WHEN processing multilingual input, THE System SHALL correctly identify the language before processing content
7. WHEN processing fails, THE System SHALL provide helpful error messages in the patient's Language_Preference

### Requirement 13: Continuous Care Loop

**User Story:** As a patient, I want the system to guide me through the complete healthcare journey from symptoms to recovery, so that I receive continuous support throughout my treatment.

#### Acceptance Criteria

1. WHEN a patient completes symptom input, THE System SHALL automatically proceed to severity classification
2. WHEN severity classification is complete, THE System SHALL automatically provide care navigation
3. WHEN a patient uploads consultation information, THE System SHALL automatically generate a Consultation_Summary and Medication_Plan
4. WHEN a Medication_Plan is created, THE System SHALL automatically begin sending reminders
5. WHEN medication reminders are active, THE System SHALL automatically schedule recovery monitoring check-ins
6. WHEN recovery monitoring indicates condition changes, THE System SHALL automatically perform reclassification
7. THE System SHALL maintain continuity across all six steps of the healthcare journey without requiring the patient to restart the process
