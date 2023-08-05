"Main interface for rekognition service Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3.type_defs import Literal, overload

# pylint: disable=import-self
import mypy_boto3_rekognition.client as client_scope

# pylint: disable=import-self
import mypy_boto3_rekognition.paginator as paginator_scope
from mypy_boto3_rekognition.type_defs import (
    ClientCompareFacesResponseTypeDef,
    ClientCompareFacesSourceImageTypeDef,
    ClientCompareFacesTargetImageTypeDef,
    ClientCreateCollectionResponseTypeDef,
    ClientCreateProjectResponseTypeDef,
    ClientCreateProjectVersionOutputConfigTypeDef,
    ClientCreateProjectVersionResponseTypeDef,
    ClientCreateProjectVersionTestingDataTypeDef,
    ClientCreateProjectVersionTrainingDataTypeDef,
    ClientCreateStreamProcessorInputTypeDef,
    ClientCreateStreamProcessorOutputTypeDef,
    ClientCreateStreamProcessorResponseTypeDef,
    ClientCreateStreamProcessorSettingsTypeDef,
    ClientDeleteCollectionResponseTypeDef,
    ClientDeleteFacesResponseTypeDef,
    ClientDescribeCollectionResponseTypeDef,
    ClientDescribeProjectVersionsResponseTypeDef,
    ClientDescribeProjectsResponseTypeDef,
    ClientDescribeStreamProcessorResponseTypeDef,
    ClientDetectCustomLabelsImageTypeDef,
    ClientDetectCustomLabelsResponseTypeDef,
    ClientDetectFacesImageTypeDef,
    ClientDetectFacesResponseTypeDef,
    ClientDetectLabelsImageTypeDef,
    ClientDetectLabelsResponseTypeDef,
    ClientDetectModerationLabelsHumanLoopConfigTypeDef,
    ClientDetectModerationLabelsImageTypeDef,
    ClientDetectModerationLabelsResponseTypeDef,
    ClientDetectTextImageTypeDef,
    ClientDetectTextResponseTypeDef,
    ClientGetCelebrityInfoResponseTypeDef,
    ClientGetCelebrityRecognitionResponseTypeDef,
    ClientGetContentModerationResponseTypeDef,
    ClientGetFaceDetectionResponseTypeDef,
    ClientGetFaceSearchResponseTypeDef,
    ClientGetLabelDetectionResponseTypeDef,
    ClientGetPersonTrackingResponseTypeDef,
    ClientIndexFacesImageTypeDef,
    ClientIndexFacesResponseTypeDef,
    ClientListCollectionsResponseTypeDef,
    ClientListFacesResponseTypeDef,
    ClientListStreamProcessorsResponseTypeDef,
    ClientRecognizeCelebritiesImageTypeDef,
    ClientRecognizeCelebritiesResponseTypeDef,
    ClientSearchFacesByImageImageTypeDef,
    ClientSearchFacesByImageResponseTypeDef,
    ClientSearchFacesResponseTypeDef,
    ClientStartCelebrityRecognitionNotificationChannelTypeDef,
    ClientStartCelebrityRecognitionResponseTypeDef,
    ClientStartCelebrityRecognitionVideoTypeDef,
    ClientStartContentModerationNotificationChannelTypeDef,
    ClientStartContentModerationResponseTypeDef,
    ClientStartContentModerationVideoTypeDef,
    ClientStartFaceDetectionNotificationChannelTypeDef,
    ClientStartFaceDetectionResponseTypeDef,
    ClientStartFaceDetectionVideoTypeDef,
    ClientStartFaceSearchNotificationChannelTypeDef,
    ClientStartFaceSearchResponseTypeDef,
    ClientStartFaceSearchVideoTypeDef,
    ClientStartLabelDetectionNotificationChannelTypeDef,
    ClientStartLabelDetectionResponseTypeDef,
    ClientStartLabelDetectionVideoTypeDef,
    ClientStartPersonTrackingNotificationChannelTypeDef,
    ClientStartPersonTrackingResponseTypeDef,
    ClientStartPersonTrackingVideoTypeDef,
    ClientStartProjectVersionResponseTypeDef,
    ClientStopProjectVersionResponseTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_rekognition.waiter as waiter_scope


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def compare_faces(
        self,
        SourceImage: ClientCompareFacesSourceImageTypeDef,
        TargetImage: ClientCompareFacesTargetImageTypeDef,
        SimilarityThreshold: Any = None,
        QualityFilter: Literal["NONE", "AUTO", "LOW", "MEDIUM", "HIGH"] = None,
    ) -> ClientCompareFacesResponseTypeDef:
        """
        Compares a face in the *source* input image with each of the 100 largest faces detected in
        the *target* input image.

        .. note::

          If the source image contains multiple faces, the service detects the largest face and
          compares it with each face detected in the target image.

        You pass the input and target images either as base64-encoded image bytes or as references
        to images in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition
        operations, passing image bytes isn't supported. The image must be formatted as a PNG or
        JPEG file.

        In response, the operation returns an array of face matches ordered by similarity score in
        descending order. For each face match, the response provides a bounding box of the face,
        facial landmarks, pose details (pitch, role, and yaw), quality (brightness and sharpness),
        and confidence value (indicating the level of confidence that the bounding box contains a
        face). The response also provides a similarity score, which indicates how closely the faces
        match.

        .. note::

          By default, only faces with a similarity score of greater than or equal to 80% are
          returned in the response. You can change this value by specifying the
          ``SimilarityThreshold`` parameter.

         ``CompareFaces`` also returns an array of faces that don't match the source image. For each
         face, it returns a bounding box, confidence value, landmarks, pose details, and quality.
         The response also returns information about the face in the source image, including the
         bounding box of the face and confidence value.

        The ``QualityFilter`` input parameter allows you to filter out detected faces that don’t
        meet a required quality bar. The quality bar is based on a variety of common use cases. Use
        ``QualityFilter`` to set the quality bar by specifying ``LOW`` , ``MEDIUM`` , or ``HIGH`` .
        If you do not want to filter detected faces, specify ``NONE`` . The default value is
        ``NONE`` .

        .. note::

          To use quality filtering, you need a collection associated with version 3 of the face
          model or higher. To get the version of the face model associated with a collection, call
          DescribeCollection .

        If the image doesn't contain Exif metadata, ``CompareFaces`` returns orientation information
        for the source and target images. Use these values to display the images with the correct
        image orientation.

        If no faces are detected in the source or target images, ``CompareFaces`` returns an
        ``InvalidParameterException`` error.

        .. note::

          This is a stateless API operation. That is, data returned by this operation doesn't
          persist.

        For an example, see Comparing Faces in Images in the Amazon Rekognition Developer Guide.

        This operation requires permissions to perform the ``rekognition:CompareFaces`` action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/CompareFaces>`_

        **Request Syntax**
        ::

          response = client.compare_faces(
              SourceImage={
                  'Bytes': b'bytes',
                  'S3Object': {
                      'Bucket': 'string',
                      'Name': 'string',
                      'Version': 'string'
                  }
              },
              TargetImage={
                  'Bytes': b'bytes',
                  'S3Object': {
                      'Bucket': 'string',
                      'Name': 'string',
                      'Version': 'string'
                  }
              },
              SimilarityThreshold=...,
              QualityFilter='NONE'|'AUTO'|'LOW'|'MEDIUM'|'HIGH'
          )
        :type SourceImage: dict
        :param SourceImage: **[REQUIRED]**

          The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call
          Amazon Rekognition operations, passing base64-encoded image bytes is not supported.

          If you are using an AWS SDK to call Amazon Rekognition, you might not need to
          base64-encode image bytes passed using the ``Bytes`` field. For more information, see
          Images in the Amazon Rekognition developer guide.

          - **Bytes** *(bytes) --*

            Blob of image bytes up to 5 MBs.

          - **S3Object** *(dict) --*

            Identifies an S3 object as the image source.

            - **Bucket** *(string) --*

              Name of the S3 bucket.

            - **Name** *(string) --*

              S3 object key name.

            - **Version** *(string) --*

              If the bucket is versioning enabled, you can specify the object version.

        :type TargetImage: dict
        :param TargetImage: **[REQUIRED]**

          The target image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call
          Amazon Rekognition operations, passing base64-encoded image bytes is not supported.

          If you are using an AWS SDK to call Amazon Rekognition, you might not need to
          base64-encode image bytes passed using the ``Bytes`` field. For more information, see
          Images in the Amazon Rekognition developer guide.

          - **Bytes** *(bytes) --*

            Blob of image bytes up to 5 MBs.

          - **S3Object** *(dict) --*

            Identifies an S3 object as the image source.

            - **Bucket** *(string) --*

              Name of the S3 bucket.

            - **Name** *(string) --*

              S3 object key name.

            - **Version** *(string) --*

              If the bucket is versioning enabled, you can specify the object version.

        :type SimilarityThreshold: float
        :param SimilarityThreshold:

          The minimum level of confidence in the face matches that a match must meet to be included
          in the ``FaceMatches`` array.

        :type QualityFilter: string
        :param QualityFilter:

          A filter that specifies a quality bar for how much filtering is done to identify faces.
          Filtered faces aren't compared. If you specify ``AUTO`` , Amazon Rekognition chooses the
          quality bar. If you specify ``LOW`` , ``MEDIUM`` , or ``HIGH`` , filtering removes all
          faces that don’t meet the chosen quality bar. The quality bar is based on a variety of
          common use cases. Low-quality detections can occur for a number of reasons. Some examples
          are an object that's misidentified as a face, a face that's too blurry, or a face with a
          pose that's too extreme to use. If you specify ``NONE`` , no filtering is performed. The
          default value is ``NONE`` .

          To use quality filtering, the collection you are using must be associated with version 3
          of the face model or higher.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'SourceImageFace': {
                    'BoundingBox': {
                        'Width': ...,
                        'Height': ...,
                        'Left': ...,
                        'Top': ...
                    },
                    'Confidence': ...
                },
                'FaceMatches': [
                    {
                        'Similarity': ...,
                        'Face': {
                            'BoundingBox': {
                                'Width': ...,
                                'Height': ...,
                                'Left': ...,
                                'Top': ...
                            },
                            'Confidence': ...,
                            'Landmarks': [
                                {
                                    'Type':
                                    'eyeLeft'|'eyeRight'|'nose'
                                    |'mouthLeft'|'mouthRight'
                                    |'leftEyeBrowLeft'
                                    |'leftEyeBrowRight'|'leftEyeBrowUp'
                                    |'rightEyeBrowLeft'
                                    |'rightEyeBrowRight'
                                    |'rightEyeBrowUp'|'leftEyeLeft'
                                    |'leftEyeRight'|'leftEyeUp'
                                    |'leftEyeDown'|'rightEyeLeft'
                                    |'rightEyeRight'|'rightEyeUp'
                                    |'rightEyeDown'|'noseLeft'
                                    |'noseRight'|'mouthUp'|'mouthDown'
                                    |'leftPupil'|'rightPupil'
                                    |'upperJawlineLeft'|'midJawlineLeft'
                                    |'chinBottom'|'midJawlineRight'
                                    |'upperJawlineRight',
                                    'X': ...,
                                    'Y': ...
                                },
                            ],
                            'Pose': {
                                'Roll': ...,
                                'Yaw': ...,
                                'Pitch': ...
                            },
                            'Quality': {
                                'Brightness': ...,
                                'Sharpness': ...
                            }
                        }
                    },
                ],
                'UnmatchedFaces': [
                    {
                        'BoundingBox': {
                            'Width': ...,
                            'Height': ...,
                            'Left': ...,
                            'Top': ...
                        },
                        'Confidence': ...,
                        'Landmarks': [
                            {
                                'Type':
                                'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'
                                |'mouthRight'|'leftEyeBrowLeft'
                                |'leftEyeBrowRight'|'leftEyeBrowUp'
                                |'rightEyeBrowLeft'|'rightEyeBrowRight'
                                |'rightEyeBrowUp'|'leftEyeLeft'
                                |'leftEyeRight'|'leftEyeUp'|'leftEyeDown'
                                |'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'
                                |'rightEyeDown'|'noseLeft'|'noseRight'
                                |'mouthUp'|'mouthDown'|'leftPupil'
                                |'rightPupil'|'upperJawlineLeft'
                                |'midJawlineLeft'|'chinBottom'
                                |'midJawlineRight'|'upperJawlineRight',
                                'X': ...,
                                'Y': ...
                            },
                        ],
                        'Pose': {
                            'Roll': ...,
                            'Yaw': ...,
                            'Pitch': ...
                        },
                        'Quality': {
                            'Brightness': ...,
                            'Sharpness': ...
                        }
                    },
                ],
                'SourceImageOrientationCorrection':
                'ROTATE_0'|'ROTATE_90'|'ROTATE_180'|'ROTATE_270',
                'TargetImageOrientationCorrection': 'ROTATE_0'|'ROTATE_90'|'ROTATE_180'|'ROTATE_270'
            }
          **Response Structure**

          - *(dict) --*

            - **SourceImageFace** *(dict) --*

              The face in the source image that was used for comparison.

              - **BoundingBox** *(dict) --*

                Bounding box of the face.

                - **Width** *(float) --*

                  Width of the bounding box as a ratio of the overall image width.

                - **Height** *(float) --*

                  Height of the bounding box as a ratio of the overall image height.

                - **Left** *(float) --*

                  Left coordinate of the bounding box as a ratio of overall image width.

                - **Top** *(float) --*

                  Top coordinate of the bounding box as a ratio of overall image height.

              - **Confidence** *(float) --*

                Confidence level that the selected bounding box contains a face.

            - **FaceMatches** *(list) --*

              An array of faces in the target image that match the source image face. Each
              ``CompareFacesMatch`` object provides the bounding box, the confidence level that the
              bounding box contains a face, and the similarity score for the face in the bounding
              box and the face in the source image.

              - *(dict) --*

                Provides information about a face in a target image that matches the source image
                face analyzed by ``CompareFaces`` . The ``Face`` property contains the bounding box
                of the face in the target image. The ``Similarity`` property is the confidence that
                the source image face matches the face in the bounding box.

                - **Similarity** *(float) --*

                  Level of confidence that the faces match.

                - **Face** *(dict) --*

                  Provides face metadata (bounding box and confidence that the bounding box actually
                  contains a face).

                  - **BoundingBox** *(dict) --*

                    Bounding box of the face.

                    - **Width** *(float) --*

                      Width of the bounding box as a ratio of the overall image width.

                    - **Height** *(float) --*

                      Height of the bounding box as a ratio of the overall image height.

                    - **Left** *(float) --*

                      Left coordinate of the bounding box as a ratio of overall image width.

                    - **Top** *(float) --*

                      Top coordinate of the bounding box as a ratio of overall image height.

                  - **Confidence** *(float) --*

                    Level of confidence that what the bounding box contains is a face.

                  - **Landmarks** *(list) --*

                    An array of facial landmarks.

                    - *(dict) --*

                      Indicates the location of the landmark on the face.

                      - **Type** *(string) --*

                        Type of landmark.

                      - **X** *(float) --*

                        The x-coordinate from the top left of the landmark expressed as the ratio of
                        the width of the image. For example, if the image is 700 x 200 and the
                        x-coordinate of the landmark is at 350 pixels, this value is 0.5.

                      - **Y** *(float) --*

                        The y-coordinate from the top left of the landmark expressed as the ratio of
                        the height of the image. For example, if the image is 700 x 200 and the
                        y-coordinate of the landmark is at 100 pixels, this value is 0.5.

                  - **Pose** *(dict) --*

                    Indicates the pose of the face as determined by its pitch, roll, and yaw.

                    - **Roll** *(float) --*

                      Value representing the face rotation on the roll axis.

                    - **Yaw** *(float) --*

                      Value representing the face rotation on the yaw axis.

                    - **Pitch** *(float) --*

                      Value representing the face rotation on the pitch axis.

                  - **Quality** *(dict) --*

                    Identifies face image brightness and sharpness.

                    - **Brightness** *(float) --*

                      Value representing brightness of the face. The service returns a value between
                      0 and 100 (inclusive). A higher value indicates a brighter face image.

                    - **Sharpness** *(float) --*

                      Value representing sharpness of the face. The service returns a value between
                      0 and 100 (inclusive). A higher value indicates a sharper face image.

            - **UnmatchedFaces** *(list) --*

              An array of faces in the target image that did not match the source image face.

              - *(dict) --*

                Provides face metadata for target image faces that are analyzed by ``CompareFaces``
                and ``RecognizeCelebrities`` .

                - **BoundingBox** *(dict) --*

                  Bounding box of the face.

                  - **Width** *(float) --*

                    Width of the bounding box as a ratio of the overall image width.

                  - **Height** *(float) --*

                    Height of the bounding box as a ratio of the overall image height.

                  - **Left** *(float) --*

                    Left coordinate of the bounding box as a ratio of overall image width.

                  - **Top** *(float) --*

                    Top coordinate of the bounding box as a ratio of overall image height.

                - **Confidence** *(float) --*

                  Level of confidence that what the bounding box contains is a face.

                - **Landmarks** *(list) --*

                  An array of facial landmarks.

                  - *(dict) --*

                    Indicates the location of the landmark on the face.

                    - **Type** *(string) --*

                      Type of landmark.

                    - **X** *(float) --*

                      The x-coordinate from the top left of the landmark expressed as the ratio of
                      the width of the image. For example, if the image is 700 x 200 and the
                      x-coordinate of the landmark is at 350 pixels, this value is 0.5.

                    - **Y** *(float) --*

                      The y-coordinate from the top left of the landmark expressed as the ratio of
                      the height of the image. For example, if the image is 700 x 200 and the
                      y-coordinate of the landmark is at 100 pixels, this value is 0.5.

                - **Pose** *(dict) --*

                  Indicates the pose of the face as determined by its pitch, roll, and yaw.

                  - **Roll** *(float) --*

                    Value representing the face rotation on the roll axis.

                  - **Yaw** *(float) --*

                    Value representing the face rotation on the yaw axis.

                  - **Pitch** *(float) --*

                    Value representing the face rotation on the pitch axis.

                - **Quality** *(dict) --*

                  Identifies face image brightness and sharpness.

                  - **Brightness** *(float) --*

                    Value representing brightness of the face. The service returns a value between 0
                    and 100 (inclusive). A higher value indicates a brighter face image.

                  - **Sharpness** *(float) --*

                    Value representing sharpness of the face. The service returns a value between 0
                    and 100 (inclusive). A higher value indicates a sharper face image.

            - **SourceImageOrientationCorrection** *(string) --*

              The value of ``SourceImageOrientationCorrection`` is always null.

              If the input image is in .jpeg format, it might contain exchangeable image file format
              (Exif) metadata that includes the image's orientation. Amazon Rekognition uses this
              orientation information to perform image correction. The bounding box coordinates are
              translated to represent object locations after the orientation information in the Exif
              metadata is used to correct the image orientation. Images in .png format don't contain
              Exif metadata.

              Amazon Rekognition doesn’t perform image correction for images in .png format and
              .jpeg images without orientation information in the image Exif metadata. The bounding
              box coordinates aren't translated and represent the object locations before the image
              is rotated.

            - **TargetImageOrientationCorrection** *(string) --*

              The value of ``TargetImageOrientationCorrection`` is always null.

              If the input image is in .jpeg format, it might contain exchangeable image file format
              (Exif) metadata that includes the image's orientation. Amazon Rekognition uses this
              orientation information to perform image correction. The bounding box coordinates are
              translated to represent object locations after the orientation information in the Exif
              metadata is used to correct the image orientation. Images in .png format don't contain
              Exif metadata.

              Amazon Rekognition doesn’t perform image correction for images in .png format and
              .jpeg images without orientation information in the image Exif metadata. The bounding
              box coordinates aren't translated and represent the object locations before the image
              is rotated.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_collection(self, CollectionId: str) -> ClientCreateCollectionResponseTypeDef:
        """
        Creates a collection in an AWS Region. You can add faces to the collection using the
        IndexFaces operation.

        For example, you might create collections, one for each of your application users. A user
        can then index faces using the ``IndexFaces`` operation and persist results in a specific
        collection. Then, a user can search the collection for faces in the user-specific container.

        When you create a collection, it is associated with the latest version of the face model
        version.

        .. note::

          Collection names are case-sensitive.

        This operation requires permissions to perform the ``rekognition:CreateCollection`` action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/CreateCollection>`_

        **Request Syntax**
        ::

          response = client.create_collection(
              CollectionId='string'
          )
        :type CollectionId: string
        :param CollectionId: **[REQUIRED]**

          ID for the collection that you are creating.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'StatusCode': 123,
                'CollectionArn': 'string',
                'FaceModelVersion': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **StatusCode** *(integer) --*

              HTTP status code indicating the result of the operation.

            - **CollectionArn** *(string) --*

              Amazon Resource Name (ARN) of the collection. You can use this to manage permissions
              on your resources.

            - **FaceModelVersion** *(string) --*

              Version number of the face detection model associated with the collection you are
              creating.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_project(self, ProjectName: str) -> ClientCreateProjectResponseTypeDef:
        """
        Creates a new Amazon Rekognition Custom Labels project. A project is a logical grouping of
        resources (images, Labels, models) and operations (training, evaluation and detection).

        This operation requires permissions to perform the ``rekognition:CreateProject`` action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/CreateProject>`_

        **Request Syntax**
        ::

          response = client.create_project(
              ProjectName='string'
          )
        :type ProjectName: string
        :param ProjectName: **[REQUIRED]**

          The name of the project to create.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ProjectArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ProjectArn** *(string) --*

              The Amazon Resource Name (ARN) of the new project. You can use the ARN to configure
              IAM access to the project.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_project_version(
        self,
        ProjectArn: str,
        VersionName: str,
        OutputConfig: ClientCreateProjectVersionOutputConfigTypeDef,
        TrainingData: ClientCreateProjectVersionTrainingDataTypeDef,
        TestingData: ClientCreateProjectVersionTestingDataTypeDef,
    ) -> ClientCreateProjectVersionResponseTypeDef:
        """
        Creates a new version of a model and begins training. Models are managed as part of an
        Amazon Rekognition Custom Labels project. You can specify one training dataset and one
        testing dataset. The response from ``CreateProjectVersion`` is an Amazon Resource Name (ARN)
        for the version of the model.

        Training takes a while to complete. You can get the current status by calling
        DescribeProjectVersions .

        Once training has successfully completed, call  DescribeProjectVersions to get the training
        results and evaluate the model.

        After evaluating the model, you start the model by calling  StartProjectVersion .

        This operation requires permissions to perform the ``rekognition:CreateProjectVersion``
        action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/CreateProjectVersion>`_

        **Request Syntax**
        ::

          response = client.create_project_version(
              ProjectArn='string',
              VersionName='string',
              OutputConfig={
                  'S3Bucket': 'string',
                  'S3KeyPrefix': 'string'
              },
              TrainingData={
                  'Assets': [
                      {
                          'GroundTruthManifest': {
                              'S3Object': {
                                  'Bucket': 'string',
                                  'Name': 'string',
                                  'Version': 'string'
                              }
                          }
                      },
                  ]
              },
              TestingData={
                  'Assets': [
                      {
                          'GroundTruthManifest': {
                              'S3Object': {
                                  'Bucket': 'string',
                                  'Name': 'string',
                                  'Version': 'string'
                              }
                          }
                      },
                  ],
                  'AutoCreate': True|False
              }
          )
        :type ProjectArn: string
        :param ProjectArn: **[REQUIRED]**

          The ARN of the Amazon Rekognition Custom Labels project that manages the model that you
          want to train.

        :type VersionName: string
        :param VersionName: **[REQUIRED]**

          A name for the version of the model. This value must be unique.

        :type OutputConfig: dict
        :param OutputConfig: **[REQUIRED]**

          The Amazon S3 location to store the results of training.

          - **S3Bucket** *(string) --*

            The S3 bucket where training output is placed.

          - **S3KeyPrefix** *(string) --*

            The prefix applied to the training output files.

        :type TrainingData: dict
        :param TrainingData: **[REQUIRED]**

          The dataset to use for training.

          - **Assets** *(list) --*

            A Sagemaker GroundTruth manifest file that contains the training images (assets).

            - *(dict) --*

              Assets are the images that you use to train and evaluate a model version. Assets are
              referenced by Sagemaker GroundTruth manifest files.

              - **GroundTruthManifest** *(dict) --*

                The S3 bucket that contains the Ground Truth manifest file.

                - **S3Object** *(dict) --*

                  Provides the S3 bucket name and object name.

                  The region for the S3 bucket containing the S3 object must match the region you
                  use for Amazon Rekognition operations.

                  For Amazon Rekognition to process an S3 object, the user must have permission to
                  access the S3 object. For more information, see Resource-Based Policies in the
                  Amazon Rekognition Developer Guide.

                  - **Bucket** *(string) --*

                    Name of the S3 bucket.

                  - **Name** *(string) --*

                    S3 object key name.

                  - **Version** *(string) --*

                    If the bucket is versioning enabled, you can specify the object version.

        :type TestingData: dict
        :param TestingData: **[REQUIRED]**

          The dataset to use for testing.

          - **Assets** *(list) --*

            The assets used for testing.

            - *(dict) --*

              Assets are the images that you use to train and evaluate a model version. Assets are
              referenced by Sagemaker GroundTruth manifest files.

              - **GroundTruthManifest** *(dict) --*

                The S3 bucket that contains the Ground Truth manifest file.

                - **S3Object** *(dict) --*

                  Provides the S3 bucket name and object name.

                  The region for the S3 bucket containing the S3 object must match the region you
                  use for Amazon Rekognition operations.

                  For Amazon Rekognition to process an S3 object, the user must have permission to
                  access the S3 object. For more information, see Resource-Based Policies in the
                  Amazon Rekognition Developer Guide.

                  - **Bucket** *(string) --*

                    Name of the S3 bucket.

                  - **Name** *(string) --*

                    S3 object key name.

                  - **Version** *(string) --*

                    If the bucket is versioning enabled, you can specify the object version.

          - **AutoCreate** *(boolean) --*

            If specified, Amazon Rekognition Custom Labels creates a testing dataset with an 80/20
            split of the training dataset.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ProjectVersionArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ProjectVersionArn** *(string) --*

              The ARN of the model version that was created. Use ``DescribeProjectVersion`` to get
              the current status of the training operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_stream_processor(
        self,
        Input: ClientCreateStreamProcessorInputTypeDef,
        Output: ClientCreateStreamProcessorOutputTypeDef,
        Name: str,
        Settings: ClientCreateStreamProcessorSettingsTypeDef,
        RoleArn: str,
    ) -> ClientCreateStreamProcessorResponseTypeDef:
        """
        Creates an Amazon Rekognition stream processor that you can use to detect and recognize
        faces in a streaming video.

        Amazon Rekognition Video is a consumer of live video from Amazon Kinesis Video Streams.
        Amazon Rekognition Video sends analysis results to Amazon Kinesis Data Streams.

        You provide as input a Kinesis video stream (``Input`` ) and a Kinesis data stream
        (``Output`` ) stream. You also specify the face recognition criteria in ``Settings`` . For
        example, the collection containing faces that you want to recognize. Use ``Name`` to assign
        an identifier for the stream processor. You use ``Name`` to manage the stream processor. For
        example, you can start processing the source video by calling  StartStreamProcessor with the
        ``Name`` field.

        After you have finished analyzing a streaming video, use  StopStreamProcessor to stop
        processing. You can delete the stream processor by calling  DeleteStreamProcessor .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/CreateStreamProcessor>`_

        **Request Syntax**
        ::

          response = client.create_stream_processor(
              Input={
                  'KinesisVideoStream': {
                      'Arn': 'string'
                  }
              },
              Output={
                  'KinesisDataStream': {
                      'Arn': 'string'
                  }
              },
              Name='string',
              Settings={
                  'FaceSearch': {
                      'CollectionId': 'string',
                      'FaceMatchThreshold': ...
                  }
              },
              RoleArn='string'
          )
        :type Input: dict
        :param Input: **[REQUIRED]**

          Kinesis video stream stream that provides the source streaming video. If you are using the
          AWS CLI, the parameter name is ``StreamProcessorInput`` .

          - **KinesisVideoStream** *(dict) --*

            The Kinesis video stream input stream for the source streaming video.

            - **Arn** *(string) --*

              ARN of the Kinesis video stream stream that streams the source video.

        :type Output: dict
        :param Output: **[REQUIRED]**

          Kinesis data stream stream to which Amazon Rekognition Video puts the analysis results. If
          you are using the AWS CLI, the parameter name is ``StreamProcessorOutput`` .

          - **KinesisDataStream** *(dict) --*

            The Amazon Kinesis Data Streams stream to which the Amazon Rekognition stream processor
            streams the analysis results.

            - **Arn** *(string) --*

              ARN of the output Amazon Kinesis Data Streams stream.

        :type Name: string
        :param Name: **[REQUIRED]**

          An identifier you assign to the stream processor. You can use ``Name`` to manage the
          stream processor. For example, you can get the current status of the stream processor by
          calling  DescribeStreamProcessor . ``Name`` is idempotent.

        :type Settings: dict
        :param Settings: **[REQUIRED]**

          Face recognition input parameters to be used by the stream processor. Includes the
          collection to use for face recognition and the face attributes to detect.

          - **FaceSearch** *(dict) --*

            Face search settings to use on a streaming video.

            - **CollectionId** *(string) --*

              The ID of a collection that contains faces that you want to search for.

            - **FaceMatchThreshold** *(float) --*

              Minimum face match confidence score that must be met to return a result for a
              recognized face. Default is 70. 0 is the lowest confidence. 100 is the highest
              confidence.

        :type RoleArn: string
        :param RoleArn: **[REQUIRED]**

          ARN of the IAM role that allows access to the stream processor.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'StreamProcessorArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **StreamProcessorArn** *(string) --*

              ARN for the newly create stream processor.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_collection(self, CollectionId: str) -> ClientDeleteCollectionResponseTypeDef:
        """
        Deletes the specified collection. Note that this operation removes all faces in the
        collection. For an example, see  delete-collection-procedure .

        This operation requires permissions to perform the ``rekognition:DeleteCollection`` action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DeleteCollection>`_

        **Request Syntax**
        ::

          response = client.delete_collection(
              CollectionId='string'
          )
        :type CollectionId: string
        :param CollectionId: **[REQUIRED]**

          ID of the collection to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'StatusCode': 123
            }
          **Response Structure**

          - *(dict) --*

            - **StatusCode** *(integer) --*

              HTTP status code that indicates the result of the operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_faces(
        self, CollectionId: str, FaceIds: List[str]
    ) -> ClientDeleteFacesResponseTypeDef:
        """
        Deletes faces from a collection. You specify a collection ID and an array of face IDs to
        remove from the collection.

        This operation requires permissions to perform the ``rekognition:DeleteFaces`` action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DeleteFaces>`_

        **Request Syntax**
        ::

          response = client.delete_faces(
              CollectionId='string',
              FaceIds=[
                  'string',
              ]
          )
        :type CollectionId: string
        :param CollectionId: **[REQUIRED]**

          Collection from which to remove the specific faces.

        :type FaceIds: list
        :param FaceIds: **[REQUIRED]**

          An array of face IDs to delete.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DeletedFaces': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **DeletedFaces** *(list) --*

              An array of strings (face IDs) of the faces that were deleted.

              - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_stream_processor(self, Name: str) -> Dict[str, Any]:
        """
        Deletes the stream processor identified by ``Name`` . You assign the value for ``Name`` when
        you create the stream processor with  CreateStreamProcessor . You might not be able to use
        the same name for a stream processor for a few seconds after calling
        ``DeleteStreamProcessor`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DeleteStreamProcessor>`_

        **Request Syntax**
        ::

          response = client.delete_stream_processor(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the stream processor you want to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_collection(self, CollectionId: str) -> ClientDescribeCollectionResponseTypeDef:
        """
        Describes the specified collection. You can use ``DescribeCollection`` to get information,
        such as the number of faces indexed into a collection and the version of the model used by
        the collection for face detection.

        For more information, see Describing a Collection in the Amazon Rekognition Developer Guide.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DescribeCollection>`_

        **Request Syntax**
        ::

          response = client.describe_collection(
              CollectionId='string'
          )
        :type CollectionId: string
        :param CollectionId: **[REQUIRED]**

          The ID of the collection to describe.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FaceCount': 123,
                'FaceModelVersion': 'string',
                'CollectionARN': 'string',
                'CreationTimestamp': datetime(2015, 1, 1)
            }
          **Response Structure**

          - *(dict) --*

            - **FaceCount** *(integer) --*

              The number of faces that are indexed into the collection. To index faces into a
              collection, use  IndexFaces .

            - **FaceModelVersion** *(string) --*

              The version of the face model that's used by the collection for face detection.

              For more information, see Model Versioning in the Amazon Rekognition Developer Guide.

            - **CollectionARN** *(string) --*

              The Amazon Resource Name (ARN) of the collection.

            - **CreationTimestamp** *(datetime) --*

              The number of milliseconds since the Unix epoch time until the creation of the
              collection. The Unix epoch time is 00:00:00 Coordinated Universal Time (UTC),
              Thursday, 1 January 1970.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_project_versions(
        self,
        ProjectArn: str,
        VersionNames: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientDescribeProjectVersionsResponseTypeDef:
        """
        Lists and describes the models in an Amazon Rekognition Custom Labels project. You can
        specify up to 10 model versions in ``ProjectVersionArns`` . If you don't specify a value,
        descriptions for all models are returned.

        This operation requires permissions to perform the ``rekognition:DescribeProjectVersions``
        action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DescribeProjectVersions>`_

        **Request Syntax**
        ::

          response = client.describe_project_versions(
              ProjectArn='string',
              VersionNames=[
                  'string',
              ],
              NextToken='string',
              MaxResults=123
          )
        :type ProjectArn: string
        :param ProjectArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the project that contains the models you want to
          describe.

        :type VersionNames: list
        :param VersionNames:

          A list of model version names that you want to describe. You can add up to 10 model
          version names to the list. If you don't specify a value, all model descriptions are
          returned.

          - *(string) --*

        :type NextToken: string
        :param NextToken:

          If the previous response was incomplete (because there is more results to retrieve),
          Amazon Rekognition Custom Labels returns a pagination token in the response. You can use
          this pagination token to retrieve the next set of results.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return per paginated call. The largest value you can
          specify is 100. If you specify a value greater than 100, a ValidationException error
          occurs. The default value is 100.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ProjectVersionDescriptions': [
                    {
                        'ProjectVersionArn': 'string',
                        'CreationTimestamp': datetime(2015, 1, 1),
                        'MinInferenceUnits': 123,
                        'Status':
                        'TRAINING_IN_PROGRESS'|'TRAINING_COMPLETED'
                        |'TRAINING_FAILED'|'STARTING'|'RUNNING'|'FAILED'|'STOPPING'
                        |'STOPPED'|'DELETING',
                        'StatusMessage': 'string',
                        'BillableTrainingTimeInSeconds': 123,
                        'TrainingEndTimestamp': datetime(2015, 1, 1),
                        'OutputConfig': {
                            'S3Bucket': 'string',
                            'S3KeyPrefix': 'string'
                        },
                        'TrainingDataResult': {
                            'Input': {
                                'Assets': [
                                    {
                                        'GroundTruthManifest': {
                                            'S3Object': {
                                                'Bucket': 'string',
                                                'Name': 'string',
                                                'Version': 'string'
                                            }
                                        }
                                    },
                                ]
                            },
                            'Output': {
                                'Assets': [
                                    {
                                        'GroundTruthManifest': {
                                            'S3Object': {
                                                'Bucket': 'string',
                                                'Name': 'string',
                                                'Version': 'string'
                                            }
                                        }
                                    },
                                ]
                            }
                        },
                        'TestingDataResult': {
                            'Input': {
                                'Assets': [
                                    {
                                        'GroundTruthManifest': {
                                            'S3Object': {
                                                'Bucket': 'string',
                                                'Name': 'string',
                                                'Version': 'string'
                                            }
                                        }
                                    },
                                ],
                                'AutoCreate': True|False
                            },
                            'Output': {
                                'Assets': [
                                    {
                                        'GroundTruthManifest': {
                                            'S3Object': {
                                                'Bucket': 'string',
                                                'Name': 'string',
                                                'Version': 'string'
                                            }
                                        }
                                    },
                                ],
                                'AutoCreate': True|False
                            }
                        },
                        'EvaluationResult': {
                            'F1Score': ...,
                            'Summary': {
                                'S3Object': {
                                    'Bucket': 'string',
                                    'Name': 'string',
                                    'Version': 'string'
                                }
                            }
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ProjectVersionDescriptions** *(list) --*

              A list of model descriptions. The list is sorted by the creation date and time of the
              model versions, latest to earliest.

              - *(dict) --*

                The description of a version of a model.

                - **ProjectVersionArn** *(string) --*

                  The Amazon Resource Name (ARN) of the model version.

                - **CreationTimestamp** *(datetime) --*

                  The Unix datetime for the date and time that training started.

                - **MinInferenceUnits** *(integer) --*

                  The minimum number of inference units used by the model. For more information, see
                  StartProjectVersion .

                - **Status** *(string) --*

                  The current status of the model version.

                - **StatusMessage** *(string) --*

                  A descriptive message for an error or warning that occurred.

                - **BillableTrainingTimeInSeconds** *(integer) --*

                  The duration, in seconds, that the model version has been billed for training.
                  This value is only returned if the model version has been successfully trained.

                - **TrainingEndTimestamp** *(datetime) --*

                  The Unix date and time that training of the model ended.

                - **OutputConfig** *(dict) --*

                  The location where training results are saved.

                  - **S3Bucket** *(string) --*

                    The S3 bucket where training output is placed.

                  - **S3KeyPrefix** *(string) --*

                    The prefix applied to the training output files.

                - **TrainingDataResult** *(dict) --*

                  The manifest file that represents the training results.

                  - **Input** *(dict) --*

                    The training assets that you supplied for training.

                    - **Assets** *(list) --*

                      A Sagemaker GroundTruth manifest file that contains the training images
                      (assets).

                      - *(dict) --*

                        Assets are the images that you use to train and evaluate a model version.
                        Assets are referenced by Sagemaker GroundTruth manifest files.

                        - **GroundTruthManifest** *(dict) --*

                          The S3 bucket that contains the Ground Truth manifest file.

                          - **S3Object** *(dict) --*

                            Provides the S3 bucket name and object name.

                            The region for the S3 bucket containing the S3 object must match the
                            region you use for Amazon Rekognition operations.

                            For Amazon Rekognition to process an S3 object, the user must have
                            permission to access the S3 object. For more information, see
                            Resource-Based Policies in the Amazon Rekognition Developer Guide.

                            - **Bucket** *(string) --*

                              Name of the S3 bucket.

                            - **Name** *(string) --*

                              S3 object key name.

                            - **Version** *(string) --*

                              If the bucket is versioning enabled, you can specify the object
                              version.

                  - **Output** *(dict) --*

                    The images (assets) that were actually trained by Amazon Rekognition Custom
                    Labels.

                    - **Assets** *(list) --*

                      A Sagemaker GroundTruth manifest file that contains the training images
                      (assets).

                      - *(dict) --*

                        Assets are the images that you use to train and evaluate a model version.
                        Assets are referenced by Sagemaker GroundTruth manifest files.

                        - **GroundTruthManifest** *(dict) --*

                          The S3 bucket that contains the Ground Truth manifest file.

                          - **S3Object** *(dict) --*

                            Provides the S3 bucket name and object name.

                            The region for the S3 bucket containing the S3 object must match the
                            region you use for Amazon Rekognition operations.

                            For Amazon Rekognition to process an S3 object, the user must have
                            permission to access the S3 object. For more information, see
                            Resource-Based Policies in the Amazon Rekognition Developer Guide.

                            - **Bucket** *(string) --*

                              Name of the S3 bucket.

                            - **Name** *(string) --*

                              S3 object key name.

                            - **Version** *(string) --*

                              If the bucket is versioning enabled, you can specify the object
                              version.

                - **TestingDataResult** *(dict) --*

                  The manifest file that represents the testing results.

                  - **Input** *(dict) --*

                    The testing dataset that was supplied for training.

                    - **Assets** *(list) --*

                      The assets used for testing.

                      - *(dict) --*

                        Assets are the images that you use to train and evaluate a model version.
                        Assets are referenced by Sagemaker GroundTruth manifest files.

                        - **GroundTruthManifest** *(dict) --*

                          The S3 bucket that contains the Ground Truth manifest file.

                          - **S3Object** *(dict) --*

                            Provides the S3 bucket name and object name.

                            The region for the S3 bucket containing the S3 object must match the
                            region you use for Amazon Rekognition operations.

                            For Amazon Rekognition to process an S3 object, the user must have
                            permission to access the S3 object. For more information, see
                            Resource-Based Policies in the Amazon Rekognition Developer Guide.

                            - **Bucket** *(string) --*

                              Name of the S3 bucket.

                            - **Name** *(string) --*

                              S3 object key name.

                            - **Version** *(string) --*

                              If the bucket is versioning enabled, you can specify the object
                              version.

                    - **AutoCreate** *(boolean) --*

                      If specified, Amazon Rekognition Custom Labels creates a testing dataset with
                      an 80/20 split of the training dataset.

                  - **Output** *(dict) --*

                    The subset of the dataset that was actually tested. Some images (assets) might
                    not be tested due to file formatting and other issues.

                    - **Assets** *(list) --*

                      The assets used for testing.

                      - *(dict) --*

                        Assets are the images that you use to train and evaluate a model version.
                        Assets are referenced by Sagemaker GroundTruth manifest files.

                        - **GroundTruthManifest** *(dict) --*

                          The S3 bucket that contains the Ground Truth manifest file.

                          - **S3Object** *(dict) --*

                            Provides the S3 bucket name and object name.

                            The region for the S3 bucket containing the S3 object must match the
                            region you use for Amazon Rekognition operations.

                            For Amazon Rekognition to process an S3 object, the user must have
                            permission to access the S3 object. For more information, see
                            Resource-Based Policies in the Amazon Rekognition Developer Guide.

                            - **Bucket** *(string) --*

                              Name of the S3 bucket.

                            - **Name** *(string) --*

                              S3 object key name.

                            - **Version** *(string) --*

                              If the bucket is versioning enabled, you can specify the object
                              version.

                    - **AutoCreate** *(boolean) --*

                      If specified, Amazon Rekognition Custom Labels creates a testing dataset with
                      an 80/20 split of the training dataset.

                - **EvaluationResult** *(dict) --*

                  The training results. ``EvaluationResult`` is only returned if training is
                  successful.

                  - **F1Score** *(float) --*

                    The F1 score for the evaluation of all labels. The F1 score metric evaluates the
                    overall precision and recall performance of the model as a single value. A
                    higher value indicates better precision and recall performance. A lower score
                    indicates that precision, recall, or both are performing poorly.

                  - **Summary** *(dict) --*

                    The S3 bucket that contains the training summary.

                    - **S3Object** *(dict) --*

                      Provides the S3 bucket name and object name.

                      The region for the S3 bucket containing the S3 object must match the region
                      you use for Amazon Rekognition operations.

                      For Amazon Rekognition to process an S3 object, the user must have permission
                      to access the S3 object. For more information, see Resource-Based Policies in
                      the Amazon Rekognition Developer Guide.

                      - **Bucket** *(string) --*

                        Name of the S3 bucket.

                      - **Name** *(string) --*

                        S3 object key name.

                      - **Version** *(string) --*

                        If the bucket is versioning enabled, you can specify the object version.

            - **NextToken** *(string) --*

              If the previous response was incomplete (because there is more results to retrieve),
              Amazon Rekognition Custom Labels returns a pagination token in the response. You can
              use this pagination token to retrieve the next set of results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_projects(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientDescribeProjectsResponseTypeDef:
        """
        Lists and gets information about your Amazon Rekognition Custom Labels projects.

        This operation requires permissions to perform the ``rekognition:DescribeProjects`` action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DescribeProjects>`_

        **Request Syntax**
        ::

          response = client.describe_projects(
              NextToken='string',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken:

          If the previous response was incomplete (because there is more results to retrieve),
          Amazon Rekognition Custom Labels returns a pagination token in the response. You can use
          this pagination token to retrieve the next set of results.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return per paginated call. The largest value you can
          specify is 100. If you specify a value greater than 100, a ValidationException error
          occurs. The default value is 100.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ProjectDescriptions': [
                    {
                        'ProjectArn': 'string',
                        'CreationTimestamp': datetime(2015, 1, 1),
                        'Status': 'CREATING'|'CREATED'|'DELETING'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ProjectDescriptions** *(list) --*

              A list of project descriptions. The list is sorted by the date and time the projects
              are created.

              - *(dict) --*

                A description of a Amazon Rekognition Custom Labels project.

                - **ProjectArn** *(string) --*

                  The Amazon Resource Name (ARN) of the project.

                - **CreationTimestamp** *(datetime) --*

                  The Unix timestamp for the date and time that the project was created.

                - **Status** *(string) --*

                  The current status of the project.

            - **NextToken** *(string) --*

              If the previous response was incomplete (because there is more results to retrieve),
              Amazon Rekognition Custom Labels returns a pagination token in the response. You can
              use this pagination token to retrieve the next set of results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_stream_processor(self, Name: str) -> ClientDescribeStreamProcessorResponseTypeDef:
        """
        Provides information about a stream processor created by  CreateStreamProcessor . You can
        get information about the input and output streams, the input parameters for the face
        recognition being performed, and the current status of the stream processor.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DescribeStreamProcessor>`_

        **Request Syntax**
        ::

          response = client.describe_stream_processor(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          Name of the stream processor for which you want information.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Name': 'string',
                'StreamProcessorArn': 'string',
                'Status': 'STOPPED'|'STARTING'|'RUNNING'|'FAILED'|'STOPPING',
                'StatusMessage': 'string',
                'CreationTimestamp': datetime(2015, 1, 1),
                'LastUpdateTimestamp': datetime(2015, 1, 1),
                'Input': {
                    'KinesisVideoStream': {
                        'Arn': 'string'
                    }
                },
                'Output': {
                    'KinesisDataStream': {
                        'Arn': 'string'
                    }
                },
                'RoleArn': 'string',
                'Settings': {
                    'FaceSearch': {
                        'CollectionId': 'string',
                        'FaceMatchThreshold': ...
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Name** *(string) --*

              Name of the stream processor.

            - **StreamProcessorArn** *(string) --*

              ARN of the stream processor.

            - **Status** *(string) --*

              Current status of the stream processor.

            - **StatusMessage** *(string) --*

              Detailed status message about the stream processor.

            - **CreationTimestamp** *(datetime) --*

              Date and time the stream processor was created

            - **LastUpdateTimestamp** *(datetime) --*

              The time, in Unix format, the stream processor was last updated. For example, when the
              stream processor moves from a running state to a failed state, or when the user starts
              or stops the stream processor.

            - **Input** *(dict) --*

              Kinesis video stream that provides the source streaming video.

              - **KinesisVideoStream** *(dict) --*

                The Kinesis video stream input stream for the source streaming video.

                - **Arn** *(string) --*

                  ARN of the Kinesis video stream stream that streams the source video.

            - **Output** *(dict) --*

              Kinesis data stream to which Amazon Rekognition Video puts the analysis results.

              - **KinesisDataStream** *(dict) --*

                The Amazon Kinesis Data Streams stream to which the Amazon Rekognition stream
                processor streams the analysis results.

                - **Arn** *(string) --*

                  ARN of the output Amazon Kinesis Data Streams stream.

            - **RoleArn** *(string) --*

              ARN of the IAM role that allows access to the stream processor.

            - **Settings** *(dict) --*

              Face recognition input parameters that are being used by the stream processor.
              Includes the collection to use for face recognition and the face attributes to detect.

              - **FaceSearch** *(dict) --*

                Face search settings to use on a streaming video.

                - **CollectionId** *(string) --*

                  The ID of a collection that contains faces that you want to search for.

                - **FaceMatchThreshold** *(float) --*

                  Minimum face match confidence score that must be met to return a result for a
                  recognized face. Default is 70. 0 is the lowest confidence. 100 is the highest
                  confidence.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_custom_labels(
        self,
        ProjectVersionArn: str,
        Image: ClientDetectCustomLabelsImageTypeDef,
        MaxResults: int = None,
        MinConfidence: Any = None,
    ) -> ClientDetectCustomLabelsResponseTypeDef:
        """
        Detects custom labels in a supplied image by using an Amazon Rekognition Custom Labels
        model.

        You specify which version of a model version to use by using the ``ProjectVersionArn`` input
        parameter.

        You pass the input image as base64-encoded image bytes or as a reference to an image in an
        Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing
        image bytes is not supported. The image must be either a PNG or JPEG formatted file.

        For each object that the model version detects on an image, the API returns a
        (``CustomLabel`` ) object in an array (``CustomLabels`` ). Each ``CustomLabel`` object
        provides the label name (``Name`` ), the level of confidence that the image contains the
        object (``Confidence`` ), and object location information, if it exists, for the label on
        the image (``Geometry`` ).

        During training model calculates a threshold value that determines if a prediction for a
        label is true. By default, ``DetectCustomLabels`` doesn't return labels whose confidence
        value is below the model's calculated threshold value. To filter labels that are returned,
        specify a value for ``MinConfidence`` that is higher than the model's calculated threshold.
        You can get the model's calculated threshold from the model's training results shown in the
        Amazon Rekognition Custom Labels console. To get all labels, regardless of confidence,
        specify a ``MinConfidence`` value of 0.

        You can also add the ``MaxResults`` parameter to limit the number of labels returned.

        This is a stateless API operation. That is, the operation does not persist any data.

        This operation requires permissions to perform the ``rekognition:DetectCustomLabels``
        action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DetectCustomLabels>`_

        **Request Syntax**
        ::

          response = client.detect_custom_labels(
              ProjectVersionArn='string',
              Image={
                  'Bytes': b'bytes',
                  'S3Object': {
                      'Bucket': 'string',
                      'Name': 'string',
                      'Version': 'string'
                  }
              },
              MaxResults=123,
              MinConfidence=...
          )
        :type ProjectVersionArn: string
        :param ProjectVersionArn: **[REQUIRED]**

          The ARN of the model version that you want to use.

        :type Image: dict
        :param Image: **[REQUIRED]**

          Provides the input image either as bytes or an S3 object.

          You pass image bytes to an Amazon Rekognition API operation by using the ``Bytes``
          property. For example, you would use the ``Bytes`` property to pass an image loaded from a
          local file system. Image bytes passed by using the ``Bytes`` property must be
          base64-encoded. Your code may not need to encode image bytes if you are using an AWS SDK
          to call Amazon Rekognition API operations.

          For more information, see Analyzing an Image Loaded from a Local File System in the Amazon
          Rekognition Developer Guide.

          You pass images stored in an S3 bucket to an Amazon Rekognition API operation by using the
          ``S3Object`` property. Images stored in an S3 bucket do not need to be base64-encoded.

          The region for the S3 bucket containing the S3 object must match the region you use for
          Amazon Rekognition operations.

          If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes using
          the Bytes property is not supported. You must first upload the image to an Amazon S3
          bucket and then call the operation using the S3Object property.

          For Amazon Rekognition to process an S3 object, the user must have permission to access
          the S3 object. For more information, see Resource Based Policies in the Amazon Rekognition
          Developer Guide.

          - **Bytes** *(bytes) --*

            Blob of image bytes up to 5 MBs.

          - **S3Object** *(dict) --*

            Identifies an S3 object as the image source.

            - **Bucket** *(string) --*

              Name of the S3 bucket.

            - **Name** *(string) --*

              S3 object key name.

            - **Version** *(string) --*

              If the bucket is versioning enabled, you can specify the object version.

        :type MaxResults: integer
        :param MaxResults:

          Maximum number of results you want the service to return in the response. The service
          returns the specified number of highest confidence labels ranked from highest confidence
          to lowest.

        :type MinConfidence: float
        :param MinConfidence:

          Specifies the minimum confidence level for the labels to return. Amazon Rekognition
          doesn't return any labels with a confidence lower than this specified value. If you
          specify a value of 0, all labels are return, regardless of the default thresholds that the
          model version applies.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CustomLabels': [
                    {
                        'Name': 'string',
                        'Confidence': ...,
                        'Geometry': {
                            'BoundingBox': {
                                'Width': ...,
                                'Height': ...,
                                'Left': ...,
                                'Top': ...
                            },
                            'Polygon': [
                                {
                                    'X': ...,
                                    'Y': ...
                                },
                            ]
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **CustomLabels** *(list) --*

              An array of custom labels detected in the input image.

              - *(dict) --*

                A custom label detected in an image by a call to  DetectCustomLabels .

                - **Name** *(string) --*

                  The name of the custom label.

                - **Confidence** *(float) --*

                  The confidence that the model has in the detection of the custom label. The range
                  is 0-100. A higher value indicates a higher confidence.

                - **Geometry** *(dict) --*

                  The location of the detected object on the image that corresponds to the custom
                  label. Includes an axis aligned coarse bounding box surrounding the object and a
                  finer grain polygon for more accurate spatial information.

                  - **BoundingBox** *(dict) --*

                    An axis-aligned coarse representation of the detected item's location on the
                    image.

                    - **Width** *(float) --*

                      Width of the bounding box as a ratio of the overall image width.

                    - **Height** *(float) --*

                      Height of the bounding box as a ratio of the overall image height.

                    - **Left** *(float) --*

                      Left coordinate of the bounding box as a ratio of overall image width.

                    - **Top** *(float) --*

                      Top coordinate of the bounding box as a ratio of overall image height.

                  - **Polygon** *(list) --*

                    Within the bounding box, a fine-grained polygon around the detected item.

                    - *(dict) --*

                      The X and Y coordinates of a point on an image. The X and Y values returned
                      are ratios of the overall image size. For example, if the input image is
                      700x200 and the operation returns X=0.5 and Y=
                          0.25, then the point is at the
                      (350,50) pixel coordinate on the image.

                      An array of ``Point`` objects, ``Polygon`` , is returned by  DetectText and by
                      DetectCustomLabels . ``Polygon`` represents a fine-grained polygon around a
                      detected item. For more information, see Geometry in the Amazon Rekognition
                      Developer Guide.

                      - **X** *(float) --*

                        The value of the X coordinate for a point on a ``Polygon`` .

                      - **Y** *(float) --*

                        The value of the Y coordinate for a point on a ``Polygon`` .
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_faces(
        self,
        Image: ClientDetectFacesImageTypeDef,
        Attributes: List[Literal["DEFAULT", "ALL"]] = None,
    ) -> ClientDetectFacesResponseTypeDef:
        """
        Detects faces within an image that is provided as input.

         ``DetectFaces`` detects the 100 largest faces in the image. For each face detected, the
         operation returns face details. These details include a bounding box of the face, a
         confidence value (that the bounding box contains a face), and a fixed set of attributes
         such as facial landmarks (for example, coordinates of eye and mouth), presence of beard,
         sunglasses, and so on.

        The face-detection algorithm is most effective on frontal faces. For non-frontal or obscured
        faces, the algorithm might not detect the faces or might detect faces with lower confidence.

        You pass the input image either as base64-encoded image bytes or as a reference to an image
        in an Amazon S3 bucket. If you use the to call Amazon Rekognition operations, passing image
        bytes is not supported. The image must be either a PNG or JPEG formatted file.

        .. note::

          This is a stateless API operation. That is, the operation does not persist any data.

        This operation requires permissions to perform the ``rekognition:DetectFaces`` action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DetectFaces>`_

        **Request Syntax**
        ::

          response = client.detect_faces(
              Image={
                  'Bytes': b'bytes',
                  'S3Object': {
                      'Bucket': 'string',
                      'Name': 'string',
                      'Version': 'string'
                  }
              },
              Attributes=[
                  'DEFAULT'|'ALL',
              ]
          )
        :type Image: dict
        :param Image: **[REQUIRED]**

          The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call
          Amazon Rekognition operations, passing base64-encoded image bytes is not supported.

          If you are using an AWS SDK to call Amazon Rekognition, you might not need to
          base64-encode image bytes passed using the ``Bytes`` field. For more information, see
          Images in the Amazon Rekognition developer guide.

          - **Bytes** *(bytes) --*

            Blob of image bytes up to 5 MBs.

          - **S3Object** *(dict) --*

            Identifies an S3 object as the image source.

            - **Bucket** *(string) --*

              Name of the S3 bucket.

            - **Name** *(string) --*

              S3 object key name.

            - **Version** *(string) --*

              If the bucket is versioning enabled, you can specify the object version.

        :type Attributes: list
        :param Attributes:

          An array of facial attributes you want to be returned. This can be the default list of
          attributes or all attributes. If you don't specify a value for ``Attributes`` or if you
          specify ``["DEFAULT"]`` , the API returns the following subset of facial attributes:
          ``BoundingBox`` , ``Confidence`` , ``Pose`` , ``Quality`` , and ``Landmarks`` . If you
          provide ``["ALL"]`` , all facial attributes are returned, but the operation takes longer
          to complete.

          If you provide both, ``["ALL", "DEFAULT"]`` , the service uses a logical AND operator to
          determine which attributes to return (in this case, all attributes).

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FaceDetails': [
                    {
                        'BoundingBox': {
                            'Width': ...,
                            'Height': ...,
                            'Left': ...,
                            'Top': ...
                        },
                        'AgeRange': {
                            'Low': 123,
                            'High': 123
                        },
                        'Smile': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Eyeglasses': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Sunglasses': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Gender': {
                            'Value': 'Male'|'Female',
                            'Confidence': ...
                        },
                        'Beard': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Mustache': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'EyesOpen': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'MouthOpen': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Emotions': [
                            {
                                'Type':
                                'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'
                                |'SURPRISED'|'CALM'|'UNKNOWN'|'FEAR',
                                'Confidence': ...
                            },
                        ],
                        'Landmarks': [
                            {
                                'Type':
                                'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'
                                |'mouthRight'|'leftEyeBrowLeft'
                                |'leftEyeBrowRight'|'leftEyeBrowUp'
                                |'rightEyeBrowLeft'|'rightEyeBrowRight'
                                |'rightEyeBrowUp'|'leftEyeLeft'
                                |'leftEyeRight'|'leftEyeUp'|'leftEyeDown'
                                |'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'
                                |'rightEyeDown'|'noseLeft'|'noseRight'
                                |'mouthUp'|'mouthDown'|'leftPupil'
                                |'rightPupil'|'upperJawlineLeft'
                                |'midJawlineLeft'|'chinBottom'
                                |'midJawlineRight'|'upperJawlineRight',
                                'X': ...,
                                'Y': ...
                            },
                        ],
                        'Pose': {
                            'Roll': ...,
                            'Yaw': ...,
                            'Pitch': ...
                        },
                        'Quality': {
                            'Brightness': ...,
                            'Sharpness': ...
                        },
                        'Confidence': ...
                    },
                ],
                'OrientationCorrection': 'ROTATE_0'|'ROTATE_90'|'ROTATE_180'|'ROTATE_270'
            }
          **Response Structure**

          - *(dict) --*

            - **FaceDetails** *(list) --*

              Details of each face found in the image.

              - *(dict) --*

                Structure containing attributes of the face that the algorithm detected.

                A ``FaceDetail`` object contains either the default facial attributes or all facial
                attributes. The default attributes are ``BoundingBox`` , ``Confidence`` ,
                ``Landmarks`` , ``Pose`` , and ``Quality`` .

                  GetFaceDetection is the only Amazon Rekognition Video stored video operation that
                  can return a ``FaceDetail`` object with all attributes. To specify which
                  attributes to return, use the ``FaceAttributes`` input parameter for
                  StartFaceDetection . The following Amazon Rekognition Video operations return only
                  the default attributes. The corresponding Start operations don't have a
                  ``FaceAttributes`` input parameter.

                * GetCelebrityRecognition

                * GetPersonTracking

                * GetFaceSearch

                The Amazon Rekognition Image  DetectFaces and  IndexFaces operations can return all
                facial attributes. To specify which attributes to return, use the ``Attributes``
                input parameter for ``DetectFaces`` . For ``IndexFaces`` , use the
                ``DetectAttributes`` input parameter.

                - **BoundingBox** *(dict) --*

                  Bounding box of the face. Default attribute.

                  - **Width** *(float) --*

                    Width of the bounding box as a ratio of the overall image width.

                  - **Height** *(float) --*

                    Height of the bounding box as a ratio of the overall image height.

                  - **Left** *(float) --*

                    Left coordinate of the bounding box as a ratio of overall image width.

                  - **Top** *(float) --*

                    Top coordinate of the bounding box as a ratio of overall image height.

                - **AgeRange** *(dict) --*

                  The estimated age range, in years, for the face. Low represents the lowest
                  estimated age and High represents the highest estimated age.

                  - **Low** *(integer) --*

                    The lowest estimated age.

                  - **High** *(integer) --*

                    The highest estimated age.

                - **Smile** *(dict) --*

                  Indicates whether or not the face is smiling, and the confidence level in the
                  determination.

                  - **Value** *(boolean) --*

                    Boolean value that indicates whether the face is smiling or not.

                  - **Confidence** *(float) --*

                    Level of confidence in the determination.

                - **Eyeglasses** *(dict) --*

                  Indicates whether or not the face is wearing eye glasses, and the confidence level
                  in the determination.

                  - **Value** *(boolean) --*

                    Boolean value that indicates whether the face is wearing eye glasses or not.

                  - **Confidence** *(float) --*

                    Level of confidence in the determination.

                - **Sunglasses** *(dict) --*

                  Indicates whether or not the face is wearing sunglasses, and the confidence level
                  in the determination.

                  - **Value** *(boolean) --*

                    Boolean value that indicates whether the face is wearing sunglasses or not.

                  - **Confidence** *(float) --*

                    Level of confidence in the determination.

                - **Gender** *(dict) --*

                  The predicted gender of a detected face.

                  - **Value** *(string) --*

                    The predicted gender of the face.

                  - **Confidence** *(float) --*

                    Level of confidence in the prediction.

                - **Beard** *(dict) --*

                  Indicates whether or not the face has a beard, and the confidence level in the
                  determination.

                  - **Value** *(boolean) --*

                    Boolean value that indicates whether the face has beard or not.

                  - **Confidence** *(float) --*

                    Level of confidence in the determination.

                - **Mustache** *(dict) --*

                  Indicates whether or not the face has a mustache, and the confidence level in the
                  determination.

                  - **Value** *(boolean) --*

                    Boolean value that indicates whether the face has mustache or not.

                  - **Confidence** *(float) --*

                    Level of confidence in the determination.

                - **EyesOpen** *(dict) --*

                  Indicates whether or not the eyes on the face are open, and the confidence level
                  in the determination.

                  - **Value** *(boolean) --*

                    Boolean value that indicates whether the eyes on the face are open.

                  - **Confidence** *(float) --*

                    Level of confidence in the determination.

                - **MouthOpen** *(dict) --*

                  Indicates whether or not the mouth on the face is open, and the confidence level
                  in the determination.

                  - **Value** *(boolean) --*

                    Boolean value that indicates whether the mouth on the face is open or not.

                  - **Confidence** *(float) --*

                    Level of confidence in the determination.

                - **Emotions** *(list) --*

                  The emotions that appear to be expressed on the face, and the confidence level in
                  the determination. The API is only making a determination of the physical
                  appearance of a person's face. It is not a determination of the person’s internal
                  emotional state and should not be used in such a way. For example, a person
                  pretending to have a sad face might not be sad emotionally.

                  - *(dict) --*

                    The emotions that appear to be expressed on the face, and the confidence level
                    in the determination. The API is only making a determination of the physical
                    appearance of a person's face. It is not a determination of the person’s
                    internal emotional state and should not be used in such a way. For example, a
                    person pretending to have a sad face might not be sad emotionally.

                    - **Type** *(string) --*

                      Type of emotion detected.

                    - **Confidence** *(float) --*

                      Level of confidence in the determination.

                - **Landmarks** *(list) --*

                  Indicates the location of landmarks on the face. Default attribute.

                  - *(dict) --*

                    Indicates the location of the landmark on the face.

                    - **Type** *(string) --*

                      Type of landmark.

                    - **X** *(float) --*

                      The x-coordinate from the top left of the landmark expressed as the ratio of
                      the width of the image. For example, if the image is 700 x 200 and the
                      x-coordinate of the landmark is at 350 pixels, this value is 0.5.

                    - **Y** *(float) --*

                      The y-coordinate from the top left of the landmark expressed as the ratio of
                      the height of the image. For example, if the image is 700 x 200 and the
                      y-coordinate of the landmark is at 100 pixels, this value is 0.5.

                - **Pose** *(dict) --*

                  Indicates the pose of the face as determined by its pitch, roll, and yaw. Default
                  attribute.

                  - **Roll** *(float) --*

                    Value representing the face rotation on the roll axis.

                  - **Yaw** *(float) --*

                    Value representing the face rotation on the yaw axis.

                  - **Pitch** *(float) --*

                    Value representing the face rotation on the pitch axis.

                - **Quality** *(dict) --*

                  Identifies image brightness and sharpness. Default attribute.

                  - **Brightness** *(float) --*

                    Value representing brightness of the face. The service returns a value between 0
                    and 100 (inclusive). A higher value indicates a brighter face image.

                  - **Sharpness** *(float) --*

                    Value representing sharpness of the face. The service returns a value between 0
                    and 100 (inclusive). A higher value indicates a sharper face image.

                - **Confidence** *(float) --*

                  Confidence level that the bounding box contains a face (and not a different object
                  such as a tree). Default attribute.

            - **OrientationCorrection** *(string) --*

              The value of ``OrientationCorrection`` is always null.

              If the input image is in .jpeg format, it might contain exchangeable image file format
              (Exif) metadata that includes the image's orientation. Amazon Rekognition uses this
              orientation information to perform image correction. The bounding box coordinates are
              translated to represent object locations after the orientation information in the Exif
              metadata is used to correct the image orientation. Images in .png format don't contain
              Exif metadata.

              Amazon Rekognition doesn’t perform image correction for images in .png format and
              .jpeg images without orientation information in the image Exif metadata. The bounding
              box coordinates aren't translated and represent the object locations before the image
              is rotated.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_labels(
        self,
        Image: ClientDetectLabelsImageTypeDef,
        MaxLabels: int = None,
        MinConfidence: Any = None,
    ) -> ClientDetectLabelsResponseTypeDef:
        """
        Detects instances of real-world entities within an image (JPEG or PNG) provided as input.
        This includes objects like flower, tree, and table; events like wedding, graduation, and
        birthday party; and concepts like landscape, evening, and nature.

        For an example, see Analyzing Images Stored in an Amazon S3 Bucket in the Amazon Rekognition
        Developer Guide.

        .. note::

           ``DetectLabels`` does not support the detection of activities. However, activity
           detection is supported for label detection in videos. For more information, see
           StartLabelDetection in the Amazon Rekognition Developer Guide.

        You pass the input image as base64-encoded image bytes or as a reference to an image in an
        Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing
        image bytes is not supported. The image must be either a PNG or JPEG formatted file.

        For each object, scene, and concept the API returns one or more labels. Each label provides
        the object name, and the level of confidence that the image contains the object. For
        example, suppose the input image has a lighthouse, the sea, and a rock. The response
        includes all three labels, one for each object.

         ``{Name: lighthouse, Confidence: 98.4629}``

         ``{Name: rock,Confidence: 79.2097}``

         ``{Name: sea,Confidence: 75.061}``

        In the preceding example, the operation returns one label for each of the three objects. The
        operation can also return multiple labels for the same object in the image. For example, if
        the input image shows a flower (for example, a tulip), the operation might return the
        following three labels.

         ``{Name: flower,Confidence: 99.0562}``

         ``{Name: plant,Confidence: 99.0562}``

         ``{Name: tulip,Confidence: 99.0562}``

        In this example, the detection algorithm more precisely identifies the flower as a tulip.

        In response, the API returns an array of labels. In addition, the response also includes the
        orientation correction. Optionally, you can specify ``MinConfidence`` to control the
        confidence threshold for the labels returned. The default is 55%. You can also add the
        ``MaxLabels`` parameter to limit the number of labels returned.

        .. note::

          If the object detected is a person, the operation doesn't provide the same facial details
          that the  DetectFaces operation provides.

         ``DetectLabels`` returns bounding boxes for instances of common object labels in an array
         of  Instance objects. An ``Instance`` object contains a  BoundingBox object, for the
         location of the label on the image. It also includes the confidence by which the bounding
         box was detected.

         ``DetectLabels`` also returns a hierarchical taxonomy of detected labels. For example, a
         detected car might be assigned the label *car* . The label *car* has two parent labels:
         *Vehicle* (its parent) and *Transportation* (its grandparent). The response returns the
         entire list of ancestors for a label. Each ancestor is a unique label in the response. In
         the previous example, *Car* , *Vehicle* , and *Transportation* are returned as unique
         labels in the response.

        This is a stateless API operation. That is, the operation does not persist any data.

        This operation requires permissions to perform the ``rekognition:DetectLabels`` action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DetectLabels>`_

        **Request Syntax**
        ::

          response = client.detect_labels(
              Image={
                  'Bytes': b'bytes',
                  'S3Object': {
                      'Bucket': 'string',
                      'Name': 'string',
                      'Version': 'string'
                  }
              },
              MaxLabels=123,
              MinConfidence=...
          )
        :type Image: dict
        :param Image: **[REQUIRED]**

          The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call
          Amazon Rekognition operations, passing image bytes is not supported. Images stored in an
          S3 Bucket do not need to be base64-encoded.

          If you are using an AWS SDK to call Amazon Rekognition, you might not need to
          base64-encode image bytes passed using the ``Bytes`` field. For more information, see
          Images in the Amazon Rekognition developer guide.

          - **Bytes** *(bytes) --*

            Blob of image bytes up to 5 MBs.

          - **S3Object** *(dict) --*

            Identifies an S3 object as the image source.

            - **Bucket** *(string) --*

              Name of the S3 bucket.

            - **Name** *(string) --*

              S3 object key name.

            - **Version** *(string) --*

              If the bucket is versioning enabled, you can specify the object version.

        :type MaxLabels: integer
        :param MaxLabels:

          Maximum number of labels you want the service to return in the response. The service
          returns the specified number of highest confidence labels.

        :type MinConfidence: float
        :param MinConfidence:

          Specifies the minimum confidence level for the labels to return. Amazon Rekognition
          doesn't return any labels with confidence lower than this specified value.

          If ``MinConfidence`` is not specified, the operation returns labels with a confidence
          values greater than or equal to 55 percent.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Labels': [
                    {
                        'Name': 'string',
                        'Confidence': ...,
                        'Instances': [
                            {
                                'BoundingBox': {
                                    'Width': ...,
                                    'Height': ...,
                                    'Left': ...,
                                    'Top': ...
                                },
                                'Confidence': ...
                            },
                        ],
                        'Parents': [
                            {
                                'Name': 'string'
                            },
                        ]
                    },
                ],
                'OrientationCorrection': 'ROTATE_0'|'ROTATE_90'|'ROTATE_180'|'ROTATE_270',
                'LabelModelVersion': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Labels** *(list) --*

              An array of labels for the real-world objects detected.

              - *(dict) --*

                Structure containing details about the detected label, including the name, detected
                instances, parent labels, and level of confidence.

                - **Name** *(string) --*

                  The name (label) of the object or scene.

                - **Confidence** *(float) --*

                  Level of confidence.

                - **Instances** *(list) --*

                  If ``Label`` represents an object, ``Instances`` contains the bounding boxes for
                  each instance of the detected object. Bounding boxes are returned for common
                  object labels such as people, cars, furniture, apparel or pets.

                  - *(dict) --*

                    An instance of a label returned by Amazon Rekognition Image ( DetectLabels ) or
                    by Amazon Rekognition Video ( GetLabelDetection ).

                    - **BoundingBox** *(dict) --*

                      The position of the label instance on the image.

                      - **Width** *(float) --*

                        Width of the bounding box as a ratio of the overall image width.

                      - **Height** *(float) --*

                        Height of the bounding box as a ratio of the overall image height.

                      - **Left** *(float) --*

                        Left coordinate of the bounding box as a ratio of overall image width.

                      - **Top** *(float) --*

                        Top coordinate of the bounding box as a ratio of overall image height.

                    - **Confidence** *(float) --*

                      The confidence that Amazon Rekognition has in the accuracy of the bounding
                      box.

                - **Parents** *(list) --*

                  The parent labels for a label. The response includes all ancestor labels.

                  - *(dict) --*

                    A parent label for a label. A label can have 0, 1, or more parents.

                    - **Name** *(string) --*

                      The name of the parent label.

            - **OrientationCorrection** *(string) --*

              The value of ``OrientationCorrection`` is always null.

              If the input image is in .jpeg format, it might contain exchangeable image file format
              (Exif) metadata that includes the image's orientation. Amazon Rekognition uses this
              orientation information to perform image correction. The bounding box coordinates are
              translated to represent object locations after the orientation information in the Exif
              metadata is used to correct the image orientation. Images in .png format don't contain
              Exif metadata.

              Amazon Rekognition doesn’t perform image correction for images in .png format and
              .jpeg images without orientation information in the image Exif metadata. The bounding
              box coordinates aren't translated and represent the object locations before the image
              is rotated.

            - **LabelModelVersion** *(string) --*

              Version number of the label detection model that was used to detect labels.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_moderation_labels(
        self,
        Image: ClientDetectModerationLabelsImageTypeDef,
        MinConfidence: Any = None,
        HumanLoopConfig: ClientDetectModerationLabelsHumanLoopConfigTypeDef = None,
    ) -> ClientDetectModerationLabelsResponseTypeDef:
        """
        Detects unsafe content in a specified JPEG or PNG format image. Use
        ``DetectModerationLabels`` to moderate images depending on your requirements. For example,
        you might want to filter images that contain nudity, but not images containing suggestive
        content.

        To filter images, use the labels returned by ``DetectModerationLabels`` to determine which
        types of content are appropriate.

        For information about moderation labels, see Detecting Unsafe Content in the Amazon
        Rekognition Developer Guide.

        You pass the input image either as base64-encoded image bytes or as a reference to an image
        in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations,
        passing image bytes is not supported. The image must be either a PNG or JPEG formatted file.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DetectModerationLabels>`_

        **Request Syntax**
        ::

          response = client.detect_moderation_labels(
              Image={
                  'Bytes': b'bytes',
                  'S3Object': {
                      'Bucket': 'string',
                      'Name': 'string',
                      'Version': 'string'
                  }
              },
              MinConfidence=...,
              HumanLoopConfig={
                  'HumanLoopName': 'string',
                  'FlowDefinitionArn': 'string',
                  'DataAttributes': {
                      'ContentClassifiers': [
                          'FreeOfPersonallyIdentifiableInformation'|'FreeOfAdultContent',
                      ]
                  }
              }
          )
        :type Image: dict
        :param Image: **[REQUIRED]**

          The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call
          Amazon Rekognition operations, passing base64-encoded image bytes is not supported.

          If you are using an AWS SDK to call Amazon Rekognition, you might not need to
          base64-encode image bytes passed using the ``Bytes`` field. For more information, see
          Images in the Amazon Rekognition developer guide.

          - **Bytes** *(bytes) --*

            Blob of image bytes up to 5 MBs.

          - **S3Object** *(dict) --*

            Identifies an S3 object as the image source.

            - **Bucket** *(string) --*

              Name of the S3 bucket.

            - **Name** *(string) --*

              S3 object key name.

            - **Version** *(string) --*

              If the bucket is versioning enabled, you can specify the object version.

        :type MinConfidence: float
        :param MinConfidence:

          Specifies the minimum confidence level for the labels to return. Amazon Rekognition
          doesn't return any labels with a confidence level lower than this specified value.

          If you don't specify ``MinConfidence`` , the operation returns labels with confidence
          values greater than or equal to 50 percent.

        :type HumanLoopConfig: dict
        :param HumanLoopConfig:

          Sets up the configuration for human evaluation, including the FlowDefinition the image
          will be sent to.

          - **HumanLoopName** *(string) --* **[REQUIRED]**

            The name of the human review used for this image. This should be kept unique within a
            region.

          - **FlowDefinitionArn** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the flow definition.

          - **DataAttributes** *(dict) --*

            Sets attributes of the input data.

            - **ContentClassifiers** *(list) --*

              Sets whether the input image is free of personally identifiable information.

              - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ModerationLabels': [
                    {
                        'Confidence': ...,
                        'Name': 'string',
                        'ParentName': 'string'
                    },
                ],
                'ModerationModelVersion': 'string',
                'HumanLoopActivationOutput': {
                    'HumanLoopArn': 'string',
                    'HumanLoopActivationReasons': [
                        'string',
                    ],
                    'HumanLoopActivationConditionsEvaluationResults': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ModerationLabels** *(list) --*

              Array of detected Moderation labels and the time, in milliseconds from the start of
              the video, they were detected.

              - *(dict) --*

                Provides information about a single type of unsafe content found in an image or
                video. Each type of moderated content has a label within a hierarchical taxonomy.
                For more information, see Detecting Unsafe Content in the Amazon Rekognition
                Developer Guide.

                - **Confidence** *(float) --*

                  Specifies the confidence that Amazon Rekognition has that the label has been
                  correctly identified.

                  If you don't specify the ``MinConfidence`` parameter in the call to
                  ``DetectModerationLabels`` , the operation returns labels with a confidence value
                  greater than or equal to 50 percent.

                - **Name** *(string) --*

                  The label name for the type of unsafe content detected in the image.

                - **ParentName** *(string) --*

                  The name for the parent label. Labels at the top level of the hierarchy have the
                  parent label ``""`` .

            - **ModerationModelVersion** *(string) --*

              Version number of the moderation detection model that was used to detect unsafe
              content.

            - **HumanLoopActivationOutput** *(dict) --*

              Shows the results of the human in the loop evaluation.

              - **HumanLoopArn** *(string) --*

                The Amazon Resource Name (ARN) of the HumanLoop created.

              - **HumanLoopActivationReasons** *(list) --*

                Shows if and why human review was needed.

                - *(string) --*

              - **HumanLoopActivationConditionsEvaluationResults** *(string) --*

                Shows the result of condition evaluations, including those conditions which
                activated a human review.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detect_text(self, Image: ClientDetectTextImageTypeDef) -> ClientDetectTextResponseTypeDef:
        """
        Detects text in the input image and converts it into machine-readable text.

        Pass the input image as base64-encoded image bytes or as a reference to an image in an
        Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, you must
        pass it as a reference to an image in an Amazon S3 bucket. For the AWS CLI, passing image
        bytes is not supported. The image must be either a .png or .jpeg formatted file.

        The ``DetectText`` operation returns text in an array of  TextDetection elements,
        ``TextDetections`` . Each ``TextDetection`` element provides information about a single word
        or line of text that was detected in the image.

        A word is one or more ISO basic latin script characters that are not separated by spaces.
        ``DetectText`` can detect up to 50 words in an image.

        A line is a string of equally spaced words. A line isn't necessarily a complete sentence.
        For example, a driver's license number is detected as a line. A line ends when there is no
        aligned text after it. Also, a line ends when there is a large gap between words, relative
        to the length of the words. This means, depending on the gap between words, Amazon
        Rekognition may detect multiple lines in text aligned in the same direction. Periods don't
        represent the end of a line. If a sentence spans multiple lines, the ``DetectText``
        operation returns multiple lines.

        To determine whether a ``TextDetection`` element is a line of text or a word, use the
        ``TextDetection`` object ``Type`` field.

        To be detected, text must be within +/- 90 degrees orientation of the horizontal axis.

        For more information, see DetectText in the Amazon Rekognition Developer Guide.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DetectText>`_

        **Request Syntax**
        ::

          response = client.detect_text(
              Image={
                  'Bytes': b'bytes',
                  'S3Object': {
                      'Bucket': 'string',
                      'Name': 'string',
                      'Version': 'string'
                  }
              }
          )
        :type Image: dict
        :param Image: **[REQUIRED]**

          The input image as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI to
          call Amazon Rekognition operations, you can't pass image bytes.

          If you are using an AWS SDK to call Amazon Rekognition, you might not need to
          base64-encode image bytes passed using the ``Bytes`` field. For more information, see
          Images in the Amazon Rekognition developer guide.

          - **Bytes** *(bytes) --*

            Blob of image bytes up to 5 MBs.

          - **S3Object** *(dict) --*

            Identifies an S3 object as the image source.

            - **Bucket** *(string) --*

              Name of the S3 bucket.

            - **Name** *(string) --*

              S3 object key name.

            - **Version** *(string) --*

              If the bucket is versioning enabled, you can specify the object version.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TextDetections': [
                    {
                        'DetectedText': 'string',
                        'Type': 'LINE'|'WORD',
                        'Id': 123,
                        'ParentId': 123,
                        'Confidence': ...,
                        'Geometry': {
                            'BoundingBox': {
                                'Width': ...,
                                'Height': ...,
                                'Left': ...,
                                'Top': ...
                            },
                            'Polygon': [
                                {
                                    'X': ...,
                                    'Y': ...
                                },
                            ]
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **TextDetections** *(list) --*

              An array of text that was detected in the input image.

              - *(dict) --*

                Information about a word or line of text detected by  DetectText .

                The ``DetectedText`` field contains the text that Amazon Rekognition detected in the
                image.

                Every word and line has an identifier (``Id`` ). Each word belongs to a line and has
                a parent identifier (``ParentId`` ) that identifies the line of text in which the
                word appears. The word ``Id`` is also an index for the word within a line of words.

                For more information, see Detecting Text in the Amazon Rekognition Developer Guide.

                - **DetectedText** *(string) --*

                  The word or line of text recognized by Amazon Rekognition.

                - **Type** *(string) --*

                  The type of text that was detected.

                - **Id** *(integer) --*

                  The identifier for the detected text. The identifier is only unique for a single
                  call to ``DetectText`` .

                - **ParentId** *(integer) --*

                  The Parent identifier for the detected text identified by the value of ``ID`` . If
                  the type of detected text is ``LINE`` , the value of ``ParentId`` is ``Null`` .

                - **Confidence** *(float) --*

                  The confidence that Amazon Rekognition has in the accuracy of the detected text
                  and the accuracy of the geometry points around the detected text.

                - **Geometry** *(dict) --*

                  The location of the detected text on the image. Includes an axis aligned coarse
                  bounding box surrounding the text and a finer grain polygon for more accurate
                  spatial information.

                  - **BoundingBox** *(dict) --*

                    An axis-aligned coarse representation of the detected item's location on the
                    image.

                    - **Width** *(float) --*

                      Width of the bounding box as a ratio of the overall image width.

                    - **Height** *(float) --*

                      Height of the bounding box as a ratio of the overall image height.

                    - **Left** *(float) --*

                      Left coordinate of the bounding box as a ratio of overall image width.

                    - **Top** *(float) --*

                      Top coordinate of the bounding box as a ratio of overall image height.

                  - **Polygon** *(list) --*

                    Within the bounding box, a fine-grained polygon around the detected item.

                    - *(dict) --*

                      The X and Y coordinates of a point on an image. The X and Y values returned
                      are ratios of the overall image size. For example, if the input image is
                      700x200 and the operation returns X=0.5 and Y=
                          0.25, then the point is at the
                      (350,50) pixel coordinate on the image.

                      An array of ``Point`` objects, ``Polygon`` , is returned by  DetectText and by
                      DetectCustomLabels . ``Polygon`` represents a fine-grained polygon around a
                      detected item. For more information, see Geometry in the Amazon Rekognition
                      Developer Guide.

                      - **X** *(float) --*

                        The value of the X coordinate for a point on a ``Polygon`` .

                      - **Y** *(float) --*

                        The value of the Y coordinate for a point on a ``Polygon`` .
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        Generate a presigned url given a client, its method, and arguments

        :type ClientMethod: string
        :param ClientMethod: The client method to presign for

        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.

        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)

        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.

        :returns: The presigned url
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_celebrity_info(self, Id: str) -> ClientGetCelebrityInfoResponseTypeDef:
        """
        Gets the name and additional information about a celebrity based on his or her Amazon
        Rekognition ID. The additional information is returned as an array of URLs. If there is no
        additional information about the celebrity, this list is empty.

        For more information, see Recognizing Celebrities in an Image in the Amazon Rekognition
        Developer Guide.

        This operation requires permissions to perform the ``rekognition:GetCelebrityInfo`` action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/GetCelebrityInfo>`_

        **Request Syntax**
        ::

          response = client.get_celebrity_info(
              Id='string'
          )
        :type Id: string
        :param Id: **[REQUIRED]**

          The ID for the celebrity. You get the celebrity ID from a call to the
          RecognizeCelebrities operation, which recognizes celebrities in an image.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Urls': [
                    'string',
                ],
                'Name': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Urls** *(list) --*

              An array of URLs pointing to additional celebrity information.

              - *(string) --*

            - **Name** *(string) --*

              The name of the celebrity.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_celebrity_recognition(
        self,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: Literal["ID", "TIMESTAMP"] = None,
    ) -> ClientGetCelebrityRecognitionResponseTypeDef:
        """
        Gets the celebrity recognition results for a Amazon Rekognition Video analysis started by
        StartCelebrityRecognition .

        Celebrity recognition in a video is an asynchronous operation. Analysis is started by a call
        to  StartCelebrityRecognition which returns a job identifier (``JobId`` ). When the
        celebrity recognition operation finishes, Amazon Rekognition Video publishes a completion
        status to the Amazon Simple Notification Service topic registered in the initial call to
        ``StartCelebrityRecognition`` . To get the results of the celebrity recognition analysis,
        first check that the status value published to the Amazon SNS topic is ``SUCCEEDED`` . If
        so, call ``GetCelebrityDetection`` and pass the job identifier (``JobId`` ) from the initial
        call to ``StartCelebrityDetection`` .

        For more information, see Working With Stored Videos in the Amazon Rekognition Developer
        Guide.

         ``GetCelebrityRecognition`` returns detected celebrities and the time(s) they are detected
         in an array (``Celebrities`` ) of  CelebrityRecognition objects. Each
         ``CelebrityRecognition`` contains information about the celebrity in a  CelebrityDetail
         object and the time, ``Timestamp`` , the celebrity was detected.

        .. note::

           ``GetCelebrityRecognition`` only returns the default facial attributes (``BoundingBox`` ,
           ``Confidence`` , ``Landmarks`` , ``Pose`` , and ``Quality`` ). The other facial
           attributes listed in the ``Face`` object of the following response syntax are not
           returned. For more information, see FaceDetail in the Amazon Rekognition Developer Guide.

        By default, the ``Celebrities`` array is sorted by time (milliseconds from the start of the
        video). You can also sort the array by celebrity by specifying the value ``ID`` in the
        ``SortBy`` input parameter.

        The ``CelebrityDetail`` object includes the celebrity identifer and additional information
        urls. If you don't store the additional information urls, you can get them later by calling
        GetCelebrityInfo with the celebrity identifer.

        No information is returned for faces not recognized as celebrities.

        Use MaxResults parameter to limit the number of labels returned. If there are more results
        than specified in ``MaxResults`` , the value of ``NextToken`` in the operation response
        contains a pagination token for getting the next set of results. To get the next page of
        results, call ``GetCelebrityDetection`` and populate the ``NextToken`` request parameter
        with the token value returned from the previous call to ``GetCelebrityRecognition`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/GetCelebrityRecognition>`_

        **Request Syntax**
        ::

          response = client.get_celebrity_recognition(
              JobId='string',
              MaxResults=123,
              NextToken='string',
              SortBy='ID'|'TIMESTAMP'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]**

          Job identifier for the required celebrity recognition analysis. You can get the job
          identifer from a call to ``StartCelebrityRecognition`` .

        :type MaxResults: integer
        :param MaxResults:

          Maximum number of results to return per paginated call. The largest value you can specify
          is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned.
          The default value is 1000.

        :type NextToken: string
        :param NextToken:

          If the previous response was incomplete (because there is more recognized celebrities to
          retrieve), Amazon Rekognition Video returns a pagination token in the response. You can
          use this pagination token to retrieve the next set of celebrities.

        :type SortBy: string
        :param SortBy:

          Sort to use for celebrities returned in ``Celebrities`` field. Specify ``ID`` to sort by
          the celebrity identifier, specify ``TIMESTAMP`` to sort by the time the celebrity was
          recognized.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
                'StatusMessage': 'string',
                'VideoMetadata': {
                    'Codec': 'string',
                    'DurationMillis': 123,
                    'Format': 'string',
                    'FrameRate': ...,
                    'FrameHeight': 123,
                    'FrameWidth': 123
                },
                'NextToken': 'string',
                'Celebrities': [
                    {
                        'Timestamp': 123,
                        'Celebrity': {
                            'Urls': [
                                'string',
                            ],
                            'Name': 'string',
                            'Id': 'string',
                            'Confidence': ...,
                            'BoundingBox': {
                                'Width': ...,
                                'Height': ...,
                                'Left': ...,
                                'Top': ...
                            },
                            'Face': {
                                'BoundingBox': {
                                    'Width': ...,
                                    'Height': ...,
                                    'Left': ...,
                                    'Top': ...
                                },
                                'AgeRange': {
                                    'Low': 123,
                                    'High': 123
                                },
                                'Smile': {
                                    'Value': True|False,
                                    'Confidence': ...
                                },
                                'Eyeglasses': {
                                    'Value': True|False,
                                    'Confidence': ...
                                },
                                'Sunglasses': {
                                    'Value': True|False,
                                    'Confidence': ...
                                },
                                'Gender': {
                                    'Value': 'Male'|'Female',
                                    'Confidence': ...
                                },
                                'Beard': {
                                    'Value': True|False,
                                    'Confidence': ...
                                },
                                'Mustache': {
                                    'Value': True|False,
                                    'Confidence': ...
                                },
                                'EyesOpen': {
                                    'Value': True|False,
                                    'Confidence': ...
                                },
                                'MouthOpen': {
                                    'Value': True|False,
                                    'Confidence': ...
                                },
                                'Emotions': [
                                    {
                                        'Type':
                                        'HAPPY'|'SAD'|'ANGRY'
                                        |'CONFUSED'|'DISGUSTED'
                                        |'SURPRISED'|'CALM'
                                        |'UNKNOWN'|'FEAR',
                                        'Confidence': ...
                                    },
                                ],
                                'Landmarks': [
                                    {
                                        'Type':
                                        'eyeLeft'|'eyeRight'|'nose'
                                        |'mouthLeft'|'mouthRight'
                                        |'leftEyeBrowLeft'
                                        |'leftEyeBrowRight'
                                        |'leftEyeBrowUp'
                                        |'rightEyeBrowLeft'
                                        |'rightEyeBrowRight'
                                        |'rightEyeBrowUp'
                                        |'leftEyeLeft'
                                        |'leftEyeRight'|'leftEyeUp'
                                        |'leftEyeDown'
                                        |'rightEyeLeft'
                                        |'rightEyeRight'
                                        |'rightEyeUp'|'rightEyeDown'
                                        |'noseLeft'|'noseRight'
                                        |'mouthUp'|'mouthDown'
                                        |'leftPupil'|'rightPupil'
                                        |'upperJawlineLeft'
                                        |'midJawlineLeft'
                                        |'chinBottom'
                                        |'midJawlineRight'
                                        |'upperJawlineRight',
                                        'X': ...,
                                        'Y': ...
                                    },
                                ],
                                'Pose': {
                                    'Roll': ...,
                                    'Yaw': ...,
                                    'Pitch': ...
                                },
                                'Quality': {
                                    'Brightness': ...,
                                    'Sharpness': ...
                                },
                                'Confidence': ...
                            }
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **JobStatus** *(string) --*

              The current status of the celebrity recognition job.

            - **StatusMessage** *(string) --*

              If the job fails, ``StatusMessage`` provides a descriptive error message.

            - **VideoMetadata** *(dict) --*

              Information about a video that Amazon Rekognition Video analyzed. ``Videometadata`` is
              returned in every page of paginated responses from a Amazon Rekognition Video
              operation.

              - **Codec** *(string) --*

                Type of compression used in the analyzed video.

              - **DurationMillis** *(integer) --*

                Length of the video in milliseconds.

              - **Format** *(string) --*

                Format of the analyzed video. Possible values are MP4, MOV and AVI.

              - **FrameRate** *(float) --*

                Number of frames per second in the video.

              - **FrameHeight** *(integer) --*

                Vertical pixel dimension of the video.

              - **FrameWidth** *(integer) --*

                Horizontal pixel dimension of the video.

            - **NextToken** *(string) --*

              If the response is truncated, Amazon Rekognition Video returns this token that you can
              use in the subsequent request to retrieve the next set of celebrities.

            - **Celebrities** *(list) --*

              Array of celebrities recognized in the video.

              - *(dict) --*

                Information about a detected celebrity and the time the celebrity was detected in a
                stored video. For more information, see GetCelebrityRecognition in the Amazon
                Rekognition Developer Guide.

                - **Timestamp** *(integer) --*

                  The time, in milliseconds from the start of the video, that the celebrity was
                  recognized.

                - **Celebrity** *(dict) --*

                  Information about a recognized celebrity.

                  - **Urls** *(list) --*

                    An array of URLs pointing to additional celebrity information.

                    - *(string) --*

                  - **Name** *(string) --*

                    The name of the celebrity.

                  - **Id** *(string) --*

                    The unique identifier for the celebrity.

                  - **Confidence** *(float) --*

                    The confidence, in percentage, that Amazon Rekognition has that the recognized
                    face is the celebrity.

                  - **BoundingBox** *(dict) --*

                    Bounding box around the body of a celebrity.

                    - **Width** *(float) --*

                      Width of the bounding box as a ratio of the overall image width.

                    - **Height** *(float) --*

                      Height of the bounding box as a ratio of the overall image height.

                    - **Left** *(float) --*

                      Left coordinate of the bounding box as a ratio of overall image width.

                    - **Top** *(float) --*

                      Top coordinate of the bounding box as a ratio of overall image height.

                  - **Face** *(dict) --*

                    Face details for the recognized celebrity.

                    - **BoundingBox** *(dict) --*

                      Bounding box of the face. Default attribute.

                      - **Width** *(float) --*

                        Width of the bounding box as a ratio of the overall image width.

                      - **Height** *(float) --*

                        Height of the bounding box as a ratio of the overall image height.

                      - **Left** *(float) --*

                        Left coordinate of the bounding box as a ratio of overall image width.

                      - **Top** *(float) --*

                        Top coordinate of the bounding box as a ratio of overall image height.

                    - **AgeRange** *(dict) --*

                      The estimated age range, in years, for the face. Low represents the lowest
                      estimated age and High represents the highest estimated age.

                      - **Low** *(integer) --*

                        The lowest estimated age.

                      - **High** *(integer) --*

                        The highest estimated age.

                    - **Smile** *(dict) --*

                      Indicates whether or not the face is smiling, and the confidence level in the
                      determination.

                      - **Value** *(boolean) --*

                        Boolean value that indicates whether the face is smiling or not.

                      - **Confidence** *(float) --*

                        Level of confidence in the determination.

                    - **Eyeglasses** *(dict) --*

                      Indicates whether or not the face is wearing eye glasses, and the confidence
                      level in the determination.

                      - **Value** *(boolean) --*

                        Boolean value that indicates whether the face is wearing eye glasses or not.

                      - **Confidence** *(float) --*

                        Level of confidence in the determination.

                    - **Sunglasses** *(dict) --*

                      Indicates whether or not the face is wearing sunglasses, and the confidence
                      level in the determination.

                      - **Value** *(boolean) --*

                        Boolean value that indicates whether the face is wearing sunglasses or not.

                      - **Confidence** *(float) --*

                        Level of confidence in the determination.

                    - **Gender** *(dict) --*

                      The predicted gender of a detected face.

                      - **Value** *(string) --*

                        The predicted gender of the face.

                      - **Confidence** *(float) --*

                        Level of confidence in the prediction.

                    - **Beard** *(dict) --*

                      Indicates whether or not the face has a beard, and the confidence level in the
                      determination.

                      - **Value** *(boolean) --*

                        Boolean value that indicates whether the face has beard or not.

                      - **Confidence** *(float) --*

                        Level of confidence in the determination.

                    - **Mustache** *(dict) --*

                      Indicates whether or not the face has a mustache, and the confidence level in
                      the determination.

                      - **Value** *(boolean) --*

                        Boolean value that indicates whether the face has mustache or not.

                      - **Confidence** *(float) --*

                        Level of confidence in the determination.

                    - **EyesOpen** *(dict) --*

                      Indicates whether or not the eyes on the face are open, and the confidence
                      level in the determination.

                      - **Value** *(boolean) --*

                        Boolean value that indicates whether the eyes on the face are open.

                      - **Confidence** *(float) --*

                        Level of confidence in the determination.

                    - **MouthOpen** *(dict) --*

                      Indicates whether or not the mouth on the face is open, and the confidence
                      level in the determination.

                      - **Value** *(boolean) --*

                        Boolean value that indicates whether the mouth on the face is open or not.

                      - **Confidence** *(float) --*

                        Level of confidence in the determination.

                    - **Emotions** *(list) --*

                      The emotions that appear to be expressed on the face, and the confidence level
                      in the determination. The API is only making a determination of the physical
                      appearance of a person's face. It is not a determination of the person’s
                      internal emotional state and should not be used in such a way. For example, a
                      person pretending to have a sad face might not be sad emotionally.

                      - *(dict) --*

                        The emotions that appear to be expressed on the face, and the confidence
                        level in the determination. The API is only making a determination of the
                        physical appearance of a person's face. It is not a determination of the
                        person’s internal emotional state and should not be used in such a way. For
                        example, a person pretending to have a sad face might not be sad
                        emotionally.

                        - **Type** *(string) --*

                          Type of emotion detected.

                        - **Confidence** *(float) --*

                          Level of confidence in the determination.

                    - **Landmarks** *(list) --*

                      Indicates the location of landmarks on the face. Default attribute.

                      - *(dict) --*

                        Indicates the location of the landmark on the face.

                        - **Type** *(string) --*

                          Type of landmark.

                        - **X** *(float) --*

                          The x-coordinate from the top left of the landmark expressed as the ratio
                          of the width of the image. For example, if the image is 700 x 200 and the
                          x-coordinate of the landmark is at 350 pixels, this value is 0.5.

                        - **Y** *(float) --*

                          The y-coordinate from the top left of the landmark expressed as the ratio
                          of the height of the image. For example, if the image is 700 x 200 and the
                          y-coordinate of the landmark is at 100 pixels, this value is 0.5.

                    - **Pose** *(dict) --*

                      Indicates the pose of the face as determined by its pitch, roll, and yaw.
                      Default attribute.

                      - **Roll** *(float) --*

                        Value representing the face rotation on the roll axis.

                      - **Yaw** *(float) --*

                        Value representing the face rotation on the yaw axis.

                      - **Pitch** *(float) --*

                        Value representing the face rotation on the pitch axis.

                    - **Quality** *(dict) --*

                      Identifies image brightness and sharpness. Default attribute.

                      - **Brightness** *(float) --*

                        Value representing brightness of the face. The service returns a value
                        between 0 and 100 (inclusive). A higher value indicates a brighter face
                        image.

                      - **Sharpness** *(float) --*

                        Value representing sharpness of the face. The service returns a value
                        between 0 and 100 (inclusive). A higher value indicates a sharper face
                        image.

                    - **Confidence** *(float) --*

                      Confidence level that the bounding box contains a face (and not a different
                      object such as a tree). Default attribute.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_content_moderation(
        self,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: Literal["NAME", "TIMESTAMP"] = None,
    ) -> ClientGetContentModerationResponseTypeDef:
        """
        Gets the unsafe content analysis results for a Amazon Rekognition Video analysis started by
        StartContentModeration .

        Unsafe content analysis of a video is an asynchronous operation. You start analysis by
        calling  StartContentModeration which returns a job identifier (``JobId`` ). When analysis
        finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple
        Notification Service topic registered in the initial call to ``StartContentModeration`` . To
        get the results of the unsafe content analysis, first check that the status value published
        to the Amazon SNS topic is ``SUCCEEDED`` . If so, call ``GetContentModeration`` and pass the
        job identifier (``JobId`` ) from the initial call to ``StartContentModeration`` .

        For more information, see Working with Stored Videos in the Amazon Rekognition Devlopers
        Guide.

         ``GetContentModeration`` returns detected unsafe content labels, and the time they are
         detected, in an array, ``ModerationLabels`` , of  ContentModerationDetection objects.

        By default, the moderated labels are returned sorted by time, in milliseconds from the start
        of the video. You can also sort them by moderated label by specifying ``NAME`` for the
        ``SortBy`` input parameter.

        Since video analysis can return a large number of results, use the ``MaxResults`` parameter
        to limit the number of labels returned in a single call to ``GetContentModeration`` . If
        there are more results than specified in ``MaxResults`` , the value of ``NextToken`` in the
        operation response contains a pagination token for getting the next set of results. To get
        the next page of results, call ``GetContentModeration`` and populate the ``NextToken``
        request parameter with the value of ``NextToken`` returned from the previous call to
        ``GetContentModeration`` .

        For more information, see Detecting Unsafe Content in the Amazon Rekognition Developer
        Guide.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/GetContentModeration>`_

        **Request Syntax**
        ::

          response = client.get_content_moderation(
              JobId='string',
              MaxResults=123,
              NextToken='string',
              SortBy='NAME'|'TIMESTAMP'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]**

          The identifier for the unsafe content job. Use ``JobId`` to identify the job in a
          subsequent call to ``GetContentModeration`` .

        :type MaxResults: integer
        :param MaxResults:

          Maximum number of results to return per paginated call. The largest value you can specify
          is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned.
          The default value is 1000.

        :type NextToken: string
        :param NextToken:

          If the previous response was incomplete (because there is more data to retrieve), Amazon
          Rekognition returns a pagination token in the response. You can use this pagination token
          to retrieve the next set of unsafe content labels.

        :type SortBy: string
        :param SortBy:

          Sort to use for elements in the ``ModerationLabelDetections`` array. Use ``TIMESTAMP`` to
          sort array elements by the time labels are detected. Use ``NAME`` to alphabetically group
          elements for a label together. Within each label group, the array element are sorted by
          detection confidence. The default sort is by ``TIMESTAMP`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
                'StatusMessage': 'string',
                'VideoMetadata': {
                    'Codec': 'string',
                    'DurationMillis': 123,
                    'Format': 'string',
                    'FrameRate': ...,
                    'FrameHeight': 123,
                    'FrameWidth': 123
                },
                'ModerationLabels': [
                    {
                        'Timestamp': 123,
                        'ModerationLabel': {
                            'Confidence': ...,
                            'Name': 'string',
                            'ParentName': 'string'
                        }
                    },
                ],
                'NextToken': 'string',
                'ModerationModelVersion': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **JobStatus** *(string) --*

              The current status of the unsafe content analysis job.

            - **StatusMessage** *(string) --*

              If the job fails, ``StatusMessage`` provides a descriptive error message.

            - **VideoMetadata** *(dict) --*

              Information about a video that Amazon Rekognition analyzed. ``Videometadata`` is
              returned in every page of paginated responses from ``GetContentModeration`` .

              - **Codec** *(string) --*

                Type of compression used in the analyzed video.

              - **DurationMillis** *(integer) --*

                Length of the video in milliseconds.

              - **Format** *(string) --*

                Format of the analyzed video. Possible values are MP4, MOV and AVI.

              - **FrameRate** *(float) --*

                Number of frames per second in the video.

              - **FrameHeight** *(integer) --*

                Vertical pixel dimension of the video.

              - **FrameWidth** *(integer) --*

                Horizontal pixel dimension of the video.

            - **ModerationLabels** *(list) --*

              The detected unsafe content labels and the time(s) they were detected.

              - *(dict) --*

                Information about an unsafe content label detection in a stored video.

                - **Timestamp** *(integer) --*

                  Time, in milliseconds from the beginning of the video, that the unsafe content
                  label was detected.

                - **ModerationLabel** *(dict) --*

                  The unsafe content label detected by in the stored video.

                  - **Confidence** *(float) --*

                    Specifies the confidence that Amazon Rekognition has that the label has been
                    correctly identified.

                    If you don't specify the ``MinConfidence`` parameter in the call to
                    ``DetectModerationLabels`` , the operation returns labels with a confidence
                    value greater than or equal to 50 percent.

                  - **Name** *(string) --*

                    The label name for the type of unsafe content detected in the image.

                  - **ParentName** *(string) --*

                    The name for the parent label. Labels at the top level of the hierarchy have the
                    parent label ``""`` .

            - **NextToken** *(string) --*

              If the response is truncated, Amazon Rekognition Video returns this token that you can
              use in the subsequent request to retrieve the next set of unsafe content labels.

            - **ModerationModelVersion** *(string) --*

              Version number of the moderation detection model that was used to detect unsafe
              content.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_face_detection(
        self, JobId: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientGetFaceDetectionResponseTypeDef:
        """
        Gets face detection results for a Amazon Rekognition Video analysis started by
        StartFaceDetection .

        Face detection with Amazon Rekognition Video is an asynchronous operation. You start face
        detection by calling  StartFaceDetection which returns a job identifier (``JobId`` ). When
        the face detection operation finishes, Amazon Rekognition Video publishes a completion
        status to the Amazon Simple Notification Service topic registered in the initial call to
        ``StartFaceDetection`` . To get the results of the face detection operation, first check
        that the status value published to the Amazon SNS topic is ``SUCCEEDED`` . If so, call
        GetFaceDetection and pass the job identifier (``JobId`` ) from the initial call to
        ``StartFaceDetection`` .

         ``GetFaceDetection`` returns an array of detected faces (``Faces`` ) sorted by the time the
         faces were detected.

        Use MaxResults parameter to limit the number of labels returned. If there are more results
        than specified in ``MaxResults`` , the value of ``NextToken`` in the operation response
        contains a pagination token for getting the next set of results. To get the next page of
        results, call ``GetFaceDetection`` and populate the ``NextToken`` request parameter with the
        token value returned from the previous call to ``GetFaceDetection`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/GetFaceDetection>`_

        **Request Syntax**
        ::

          response = client.get_face_detection(
              JobId='string',
              MaxResults=123,
              NextToken='string'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]**

          Unique identifier for the face detection job. The ``JobId`` is returned from
          ``StartFaceDetection`` .

        :type MaxResults: integer
        :param MaxResults:

          Maximum number of results to return per paginated call. The largest value you can specify
          is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned.
          The default value is 1000.

        :type NextToken: string
        :param NextToken:

          If the previous response was incomplete (because there are more faces to retrieve), Amazon
          Rekognition Video returns a pagination token in the response. You can use this pagination
          token to retrieve the next set of faces.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
                'StatusMessage': 'string',
                'VideoMetadata': {
                    'Codec': 'string',
                    'DurationMillis': 123,
                    'Format': 'string',
                    'FrameRate': ...,
                    'FrameHeight': 123,
                    'FrameWidth': 123
                },
                'NextToken': 'string',
                'Faces': [
                    {
                        'Timestamp': 123,
                        'Face': {
                            'BoundingBox': {
                                'Width': ...,
                                'Height': ...,
                                'Left': ...,
                                'Top': ...
                            },
                            'AgeRange': {
                                'Low': 123,
                                'High': 123
                            },
                            'Smile': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Eyeglasses': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Sunglasses': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Gender': {
                                'Value': 'Male'|'Female',
                                'Confidence': ...
                            },
                            'Beard': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Mustache': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'EyesOpen': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'MouthOpen': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Emotions': [
                                {
                                    'Type':
                                    'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'
                                    |'DISGUSTED'|'SURPRISED'|'CALM'
                                    |'UNKNOWN'|'FEAR',
                                    'Confidence': ...
                                },
                            ],
                            'Landmarks': [
                                {
                                    'Type':
                                    'eyeLeft'|'eyeRight'|'nose'
                                    |'mouthLeft'|'mouthRight'
                                    |'leftEyeBrowLeft'
                                    |'leftEyeBrowRight'|'leftEyeBrowUp'
                                    |'rightEyeBrowLeft'
                                    |'rightEyeBrowRight'
                                    |'rightEyeBrowUp'|'leftEyeLeft'
                                    |'leftEyeRight'|'leftEyeUp'
                                    |'leftEyeDown'|'rightEyeLeft'
                                    |'rightEyeRight'|'rightEyeUp'
                                    |'rightEyeDown'|'noseLeft'
                                    |'noseRight'|'mouthUp'|'mouthDown'
                                    |'leftPupil'|'rightPupil'
                                    |'upperJawlineLeft'|'midJawlineLeft'
                                    |'chinBottom'|'midJawlineRight'
                                    |'upperJawlineRight',
                                    'X': ...,
                                    'Y': ...
                                },
                            ],
                            'Pose': {
                                'Roll': ...,
                                'Yaw': ...,
                                'Pitch': ...
                            },
                            'Quality': {
                                'Brightness': ...,
                                'Sharpness': ...
                            },
                            'Confidence': ...
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **JobStatus** *(string) --*

              The current status of the face detection job.

            - **StatusMessage** *(string) --*

              If the job fails, ``StatusMessage`` provides a descriptive error message.

            - **VideoMetadata** *(dict) --*

              Information about a video that Amazon Rekognition Video analyzed. ``Videometadata`` is
              returned in every page of paginated responses from a Amazon Rekognition video
              operation.

              - **Codec** *(string) --*

                Type of compression used in the analyzed video.

              - **DurationMillis** *(integer) --*

                Length of the video in milliseconds.

              - **Format** *(string) --*

                Format of the analyzed video. Possible values are MP4, MOV and AVI.

              - **FrameRate** *(float) --*

                Number of frames per second in the video.

              - **FrameHeight** *(integer) --*

                Vertical pixel dimension of the video.

              - **FrameWidth** *(integer) --*

                Horizontal pixel dimension of the video.

            - **NextToken** *(string) --*

              If the response is truncated, Amazon Rekognition returns this token that you can use
              in the subsequent request to retrieve the next set of faces.

            - **Faces** *(list) --*

              An array of faces detected in the video. Each element contains a detected face's
              details and the time, in milliseconds from the start of the video, the face was
              detected.

              - *(dict) --*

                Information about a face detected in a video analysis request and the time the face
                was detected in the video.

                - **Timestamp** *(integer) --*

                  Time, in milliseconds from the start of the video, that the face was detected.

                - **Face** *(dict) --*

                  The face properties for the detected face.

                  - **BoundingBox** *(dict) --*

                    Bounding box of the face. Default attribute.

                    - **Width** *(float) --*

                      Width of the bounding box as a ratio of the overall image width.

                    - **Height** *(float) --*

                      Height of the bounding box as a ratio of the overall image height.

                    - **Left** *(float) --*

                      Left coordinate of the bounding box as a ratio of overall image width.

                    - **Top** *(float) --*

                      Top coordinate of the bounding box as a ratio of overall image height.

                  - **AgeRange** *(dict) --*

                    The estimated age range, in years, for the face. Low represents the lowest
                    estimated age and High represents the highest estimated age.

                    - **Low** *(integer) --*

                      The lowest estimated age.

                    - **High** *(integer) --*

                      The highest estimated age.

                  - **Smile** *(dict) --*

                    Indicates whether or not the face is smiling, and the confidence level in the
                    determination.

                    - **Value** *(boolean) --*

                      Boolean value that indicates whether the face is smiling or not.

                    - **Confidence** *(float) --*

                      Level of confidence in the determination.

                  - **Eyeglasses** *(dict) --*

                    Indicates whether or not the face is wearing eye glasses, and the confidence
                    level in the determination.

                    - **Value** *(boolean) --*

                      Boolean value that indicates whether the face is wearing eye glasses or not.

                    - **Confidence** *(float) --*

                      Level of confidence in the determination.

                  - **Sunglasses** *(dict) --*

                    Indicates whether or not the face is wearing sunglasses, and the confidence
                    level in the determination.

                    - **Value** *(boolean) --*

                      Boolean value that indicates whether the face is wearing sunglasses or not.

                    - **Confidence** *(float) --*

                      Level of confidence in the determination.

                  - **Gender** *(dict) --*

                    The predicted gender of a detected face.

                    - **Value** *(string) --*

                      The predicted gender of the face.

                    - **Confidence** *(float) --*

                      Level of confidence in the prediction.

                  - **Beard** *(dict) --*

                    Indicates whether or not the face has a beard, and the confidence level in the
                    determination.

                    - **Value** *(boolean) --*

                      Boolean value that indicates whether the face has beard or not.

                    - **Confidence** *(float) --*

                      Level of confidence in the determination.

                  - **Mustache** *(dict) --*

                    Indicates whether or not the face has a mustache, and the confidence level in
                    the determination.

                    - **Value** *(boolean) --*

                      Boolean value that indicates whether the face has mustache or not.

                    - **Confidence** *(float) --*

                      Level of confidence in the determination.

                  - **EyesOpen** *(dict) --*

                    Indicates whether or not the eyes on the face are open, and the confidence level
                    in the determination.

                    - **Value** *(boolean) --*

                      Boolean value that indicates whether the eyes on the face are open.

                    - **Confidence** *(float) --*

                      Level of confidence in the determination.

                  - **MouthOpen** *(dict) --*

                    Indicates whether or not the mouth on the face is open, and the confidence level
                    in the determination.

                    - **Value** *(boolean) --*

                      Boolean value that indicates whether the mouth on the face is open or not.

                    - **Confidence** *(float) --*

                      Level of confidence in the determination.

                  - **Emotions** *(list) --*

                    The emotions that appear to be expressed on the face, and the confidence level
                    in the determination. The API is only making a determination of the physical
                    appearance of a person's face. It is not a determination of the person’s
                    internal emotional state and should not be used in such a way. For example, a
                    person pretending to have a sad face might not be sad emotionally.

                    - *(dict) --*

                      The emotions that appear to be expressed on the face, and the confidence level
                      in the determination. The API is only making a determination of the physical
                      appearance of a person's face. It is not a determination of the person’s
                      internal emotional state and should not be used in such a way. For example, a
                      person pretending to have a sad face might not be sad emotionally.

                      - **Type** *(string) --*

                        Type of emotion detected.

                      - **Confidence** *(float) --*

                        Level of confidence in the determination.

                  - **Landmarks** *(list) --*

                    Indicates the location of landmarks on the face. Default attribute.

                    - *(dict) --*

                      Indicates the location of the landmark on the face.

                      - **Type** *(string) --*

                        Type of landmark.

                      - **X** *(float) --*

                        The x-coordinate from the top left of the landmark expressed as the ratio of
                        the width of the image. For example, if the image is 700 x 200 and the
                        x-coordinate of the landmark is at 350 pixels, this value is 0.5.

                      - **Y** *(float) --*

                        The y-coordinate from the top left of the landmark expressed as the ratio of
                        the height of the image. For example, if the image is 700 x 200 and the
                        y-coordinate of the landmark is at 100 pixels, this value is 0.5.

                  - **Pose** *(dict) --*

                    Indicates the pose of the face as determined by its pitch, roll, and yaw.
                    Default attribute.

                    - **Roll** *(float) --*

                      Value representing the face rotation on the roll axis.

                    - **Yaw** *(float) --*

                      Value representing the face rotation on the yaw axis.

                    - **Pitch** *(float) --*

                      Value representing the face rotation on the pitch axis.

                  - **Quality** *(dict) --*

                    Identifies image brightness and sharpness. Default attribute.

                    - **Brightness** *(float) --*

                      Value representing brightness of the face. The service returns a value between
                      0 and 100 (inclusive). A higher value indicates a brighter face image.

                    - **Sharpness** *(float) --*

                      Value representing sharpness of the face. The service returns a value between
                      0 and 100 (inclusive). A higher value indicates a sharper face image.

                  - **Confidence** *(float) --*

                    Confidence level that the bounding box contains a face (and not a different
                    object such as a tree). Default attribute.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_face_search(
        self,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: Literal["INDEX", "TIMESTAMP"] = None,
    ) -> ClientGetFaceSearchResponseTypeDef:
        """
        Gets the face search results for Amazon Rekognition Video face search started by
        StartFaceSearch . The search returns faces in a collection that match the faces of persons
        detected in a video. It also includes the time(s) that faces are matched in the video.

        Face search in a video is an asynchronous operation. You start face search by calling to
        StartFaceSearch which returns a job identifier (``JobId`` ). When the search operation
        finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple
        Notification Service topic registered in the initial call to ``StartFaceSearch`` . To get
        the search results, first check that the status value published to the Amazon SNS topic is
        ``SUCCEEDED`` . If so, call ``GetFaceSearch`` and pass the job identifier (``JobId`` ) from
        the initial call to ``StartFaceSearch`` .

        For more information, see Searching Faces in a Collection in the Amazon Rekognition
        Developer Guide.

        The search results are retured in an array, ``Persons`` , of  PersonMatch objects.
        Each``PersonMatch`` element contains details about the matching faces in the input
        collection, person information (facial attributes, bounding boxes, and person identifer) for
        the matched person, and the time the person was matched in the video.

        .. note::

           ``GetFaceSearch`` only returns the default facial attributes (``BoundingBox`` ,
           ``Confidence`` , ``Landmarks`` , ``Pose`` , and ``Quality`` ). The other facial
           attributes listed in the ``Face`` object of the following response syntax are not
           returned. For more information, see FaceDetail in the Amazon Rekognition Developer Guide.

        By default, the ``Persons`` array is sorted by the time, in milliseconds from the start of
        the video, persons are matched. You can also sort by persons by specifying ``INDEX`` for the
        ``SORTBY`` input parameter.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/GetFaceSearch>`_

        **Request Syntax**
        ::

          response = client.get_face_search(
              JobId='string',
              MaxResults=123,
              NextToken='string',
              SortBy='INDEX'|'TIMESTAMP'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]**

          The job identifer for the search request. You get the job identifier from an initial call
          to ``StartFaceSearch`` .

        :type MaxResults: integer
        :param MaxResults:

          Maximum number of results to return per paginated call. The largest value you can specify
          is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned.
          The default value is 1000.

        :type NextToken: string
        :param NextToken:

          If the previous response was incomplete (because there is more search results to
          retrieve), Amazon Rekognition Video returns a pagination token in the response. You can
          use this pagination token to retrieve the next set of search results.

        :type SortBy: string
        :param SortBy:

          Sort to use for grouping faces in the response. Use ``TIMESTAMP`` to group faces by the
          time that they are recognized. Use ``INDEX`` to sort by recognized faces.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
                'StatusMessage': 'string',
                'NextToken': 'string',
                'VideoMetadata': {
                    'Codec': 'string',
                    'DurationMillis': 123,
                    'Format': 'string',
                    'FrameRate': ...,
                    'FrameHeight': 123,
                    'FrameWidth': 123
                },
                'Persons': [
                    {
                        'Timestamp': 123,
                        'Person': {
                            'Index': 123,
                            'BoundingBox': {
                                'Width': ...,
                                'Height': ...,
                                'Left': ...,
                                'Top': ...
                            },
                            'Face': {
                                'BoundingBox': {
                                    'Width': ...,
                                    'Height': ...,
                                    'Left': ...,
                                    'Top': ...
                                },
                                'AgeRange': {
                                    'Low': 123,
                                    'High': 123
                                },
                                'Smile': {
                                    'Value': True|False,
                                    'Confidence': ...
                                },
                                'Eyeglasses': {
                                    'Value': True|False,
                                    'Confidence': ...
                                },
                                'Sunglasses': {
                                    'Value': True|False,
                                    'Confidence': ...
                                },
                                'Gender': {
                                    'Value': 'Male'|'Female',
                                    'Confidence': ...
                                },
                                'Beard': {
                                    'Value': True|False,
                                    'Confidence': ...
                                },
                                'Mustache': {
                                    'Value': True|False,
                                    'Confidence': ...
                                },
                                'EyesOpen': {
                                    'Value': True|False,
                                    'Confidence': ...
                                },
                                'MouthOpen': {
                                    'Value': True|False,
                                    'Confidence': ...
                                },
                                'Emotions': [
                                    {
                                        'Type':
                                        'HAPPY'|'SAD'|'ANGRY'
                                        |'CONFUSED'|'DISGUSTED'
                                        |'SURPRISED'|'CALM'
                                        |'UNKNOWN'|'FEAR',
                                        'Confidence': ...
                                    },
                                ],
                                'Landmarks': [
                                    {
                                        'Type':
                                        'eyeLeft'|'eyeRight'|'nose'
                                        |'mouthLeft'|'mouthRight'
                                        |'leftEyeBrowLeft'
                                        |'leftEyeBrowRight'
                                        |'leftEyeBrowUp'
                                        |'rightEyeBrowLeft'
                                        |'rightEyeBrowRight'
                                        |'rightEyeBrowUp'
                                        |'leftEyeLeft'
                                        |'leftEyeRight'|'leftEyeUp'
                                        |'leftEyeDown'
                                        |'rightEyeLeft'
                                        |'rightEyeRight'
                                        |'rightEyeUp'|'rightEyeDown'
                                        |'noseLeft'|'noseRight'
                                        |'mouthUp'|'mouthDown'
                                        |'leftPupil'|'rightPupil'
                                        |'upperJawlineLeft'
                                        |'midJawlineLeft'
                                        |'chinBottom'
                                        |'midJawlineRight'
                                        |'upperJawlineRight',
                                        'X': ...,
                                        'Y': ...
                                    },
                                ],
                                'Pose': {
                                    'Roll': ...,
                                    'Yaw': ...,
                                    'Pitch': ...
                                },
                                'Quality': {
                                    'Brightness': ...,
                                    'Sharpness': ...
                                },
                                'Confidence': ...
                            }
                        },
                        'FaceMatches': [
                            {
                                'Similarity': ...,
                                'Face': {
                                    'FaceId': 'string',
                                    'BoundingBox': {
                                        'Width': ...,
                                        'Height': ...,
                                        'Left': ...,
                                        'Top': ...
                                    },
                                    'ImageId': 'string',
                                    'ExternalImageId': 'string',
                                    'Confidence': ...
                                }
                            },
                        ]
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **JobStatus** *(string) --*

              The current status of the face search job.

            - **StatusMessage** *(string) --*

              If the job fails, ``StatusMessage`` provides a descriptive error message.

            - **NextToken** *(string) --*

              If the response is truncated, Amazon Rekognition Video returns this token that you can
              use in the subsequent request to retrieve the next set of search results.

            - **VideoMetadata** *(dict) --*

              Information about a video that Amazon Rekognition analyzed. ``Videometadata`` is
              returned in every page of paginated responses from a Amazon Rekognition Video
              operation.

              - **Codec** *(string) --*

                Type of compression used in the analyzed video.

              - **DurationMillis** *(integer) --*

                Length of the video in milliseconds.

              - **Format** *(string) --*

                Format of the analyzed video. Possible values are MP4, MOV and AVI.

              - **FrameRate** *(float) --*

                Number of frames per second in the video.

              - **FrameHeight** *(integer) --*

                Vertical pixel dimension of the video.

              - **FrameWidth** *(integer) --*

                Horizontal pixel dimension of the video.

            - **Persons** *(list) --*

              An array of persons,  PersonMatch , in the video whose face(s) match the face(s) in an
              Amazon Rekognition collection. It also includes time information for when persons are
              matched in the video. You specify the input collection in an initial call to
              ``StartFaceSearch`` . Each ``Persons`` element includes a time the person was matched,
              face match details (``FaceMatches`` ) for matching faces in the collection, and person
              information (``Person`` ) for the matched person.

              - *(dict) --*

                Information about a person whose face matches a face(s) in an Amazon Rekognition
                collection. Includes information about the faces in the Amazon Rekognition
                collection ( FaceMatch ), information about the person ( PersonDetail ), and the
                time stamp for when the person was detected in a video. An array of ``PersonMatch``
                objects is returned by  GetFaceSearch .

                - **Timestamp** *(integer) --*

                  The time, in milliseconds from the beginning of the video, that the person was
                  matched in the video.

                - **Person** *(dict) --*

                  Information about the matched person.

                  - **Index** *(integer) --*

                    Identifier for the person detected person within a video. Use to keep track of
                    the person throughout the video. The identifier is not stored by Amazon
                    Rekognition.

                  - **BoundingBox** *(dict) --*

                    Bounding box around the detected person.

                    - **Width** *(float) --*

                      Width of the bounding box as a ratio of the overall image width.

                    - **Height** *(float) --*

                      Height of the bounding box as a ratio of the overall image height.

                    - **Left** *(float) --*

                      Left coordinate of the bounding box as a ratio of overall image width.

                    - **Top** *(float) --*

                      Top coordinate of the bounding box as a ratio of overall image height.

                  - **Face** *(dict) --*

                    Face details for the detected person.

                    - **BoundingBox** *(dict) --*

                      Bounding box of the face. Default attribute.

                      - **Width** *(float) --*

                        Width of the bounding box as a ratio of the overall image width.

                      - **Height** *(float) --*

                        Height of the bounding box as a ratio of the overall image height.

                      - **Left** *(float) --*

                        Left coordinate of the bounding box as a ratio of overall image width.

                      - **Top** *(float) --*

                        Top coordinate of the bounding box as a ratio of overall image height.

                    - **AgeRange** *(dict) --*

                      The estimated age range, in years, for the face. Low represents the lowest
                      estimated age and High represents the highest estimated age.

                      - **Low** *(integer) --*

                        The lowest estimated age.

                      - **High** *(integer) --*

                        The highest estimated age.

                    - **Smile** *(dict) --*

                      Indicates whether or not the face is smiling, and the confidence level in the
                      determination.

                      - **Value** *(boolean) --*

                        Boolean value that indicates whether the face is smiling or not.

                      - **Confidence** *(float) --*

                        Level of confidence in the determination.

                    - **Eyeglasses** *(dict) --*

                      Indicates whether or not the face is wearing eye glasses, and the confidence
                      level in the determination.

                      - **Value** *(boolean) --*

                        Boolean value that indicates whether the face is wearing eye glasses or not.

                      - **Confidence** *(float) --*

                        Level of confidence in the determination.

                    - **Sunglasses** *(dict) --*

                      Indicates whether or not the face is wearing sunglasses, and the confidence
                      level in the determination.

                      - **Value** *(boolean) --*

                        Boolean value that indicates whether the face is wearing sunglasses or not.

                      - **Confidence** *(float) --*

                        Level of confidence in the determination.

                    - **Gender** *(dict) --*

                      The predicted gender of a detected face.

                      - **Value** *(string) --*

                        The predicted gender of the face.

                      - **Confidence** *(float) --*

                        Level of confidence in the prediction.

                    - **Beard** *(dict) --*

                      Indicates whether or not the face has a beard, and the confidence level in the
                      determination.

                      - **Value** *(boolean) --*

                        Boolean value that indicates whether the face has beard or not.

                      - **Confidence** *(float) --*

                        Level of confidence in the determination.

                    - **Mustache** *(dict) --*

                      Indicates whether or not the face has a mustache, and the confidence level in
                      the determination.

                      - **Value** *(boolean) --*

                        Boolean value that indicates whether the face has mustache or not.

                      - **Confidence** *(float) --*

                        Level of confidence in the determination.

                    - **EyesOpen** *(dict) --*

                      Indicates whether or not the eyes on the face are open, and the confidence
                      level in the determination.

                      - **Value** *(boolean) --*

                        Boolean value that indicates whether the eyes on the face are open.

                      - **Confidence** *(float) --*

                        Level of confidence in the determination.

                    - **MouthOpen** *(dict) --*

                      Indicates whether or not the mouth on the face is open, and the confidence
                      level in the determination.

                      - **Value** *(boolean) --*

                        Boolean value that indicates whether the mouth on the face is open or not.

                      - **Confidence** *(float) --*

                        Level of confidence in the determination.

                    - **Emotions** *(list) --*

                      The emotions that appear to be expressed on the face, and the confidence level
                      in the determination. The API is only making a determination of the physical
                      appearance of a person's face. It is not a determination of the person’s
                      internal emotional state and should not be used in such a way. For example, a
                      person pretending to have a sad face might not be sad emotionally.

                      - *(dict) --*

                        The emotions that appear to be expressed on the face, and the confidence
                        level in the determination. The API is only making a determination of the
                        physical appearance of a person's face. It is not a determination of the
                        person’s internal emotional state and should not be used in such a way. For
                        example, a person pretending to have a sad face might not be sad
                        emotionally.

                        - **Type** *(string) --*

                          Type of emotion detected.

                        - **Confidence** *(float) --*

                          Level of confidence in the determination.

                    - **Landmarks** *(list) --*

                      Indicates the location of landmarks on the face. Default attribute.

                      - *(dict) --*

                        Indicates the location of the landmark on the face.

                        - **Type** *(string) --*

                          Type of landmark.

                        - **X** *(float) --*

                          The x-coordinate from the top left of the landmark expressed as the ratio
                          of the width of the image. For example, if the image is 700 x 200 and the
                          x-coordinate of the landmark is at 350 pixels, this value is 0.5.

                        - **Y** *(float) --*

                          The y-coordinate from the top left of the landmark expressed as the ratio
                          of the height of the image. For example, if the image is 700 x 200 and the
                          y-coordinate of the landmark is at 100 pixels, this value is 0.5.

                    - **Pose** *(dict) --*

                      Indicates the pose of the face as determined by its pitch, roll, and yaw.
                      Default attribute.

                      - **Roll** *(float) --*

                        Value representing the face rotation on the roll axis.

                      - **Yaw** *(float) --*

                        Value representing the face rotation on the yaw axis.

                      - **Pitch** *(float) --*

                        Value representing the face rotation on the pitch axis.

                    - **Quality** *(dict) --*

                      Identifies image brightness and sharpness. Default attribute.

                      - **Brightness** *(float) --*

                        Value representing brightness of the face. The service returns a value
                        between 0 and 100 (inclusive). A higher value indicates a brighter face
                        image.

                      - **Sharpness** *(float) --*

                        Value representing sharpness of the face. The service returns a value
                        between 0 and 100 (inclusive). A higher value indicates a sharper face
                        image.

                    - **Confidence** *(float) --*

                      Confidence level that the bounding box contains a face (and not a different
                      object such as a tree). Default attribute.

                - **FaceMatches** *(list) --*

                  Information about the faces in the input collection that match the face of a
                  person in the video.

                  - *(dict) --*

                    Provides face metadata. In addition, it also provides the confidence in the
                    match of this face with the input face.

                    - **Similarity** *(float) --*

                      Confidence in the match of this face with the input face.

                    - **Face** *(dict) --*

                      Describes the face properties such as the bounding box, face ID, image ID of
                      the source image, and external image ID that you assigned.

                      - **FaceId** *(string) --*

                        Unique identifier that Amazon Rekognition assigns to the face.

                      - **BoundingBox** *(dict) --*

                        Bounding box of the face.

                        - **Width** *(float) --*

                          Width of the bounding box as a ratio of the overall image width.

                        - **Height** *(float) --*

                          Height of the bounding box as a ratio of the overall image height.

                        - **Left** *(float) --*

                          Left coordinate of the bounding box as a ratio of overall image width.

                        - **Top** *(float) --*

                          Top coordinate of the bounding box as a ratio of overall image height.

                      - **ImageId** *(string) --*

                        Unique identifier that Amazon Rekognition assigns to the input image.

                      - **ExternalImageId** *(string) --*

                        Identifier that you assign to all the faces in the input image.

                      - **Confidence** *(float) --*

                        Confidence level that the bounding box contains a face (and not a different
                        object such as a tree).
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_label_detection(
        self,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: Literal["NAME", "TIMESTAMP"] = None,
    ) -> ClientGetLabelDetectionResponseTypeDef:
        """
        Gets the label detection results of a Amazon Rekognition Video analysis started by
        StartLabelDetection .

        The label detection operation is started by a call to  StartLabelDetection which returns a
        job identifier (``JobId`` ). When the label detection operation finishes, Amazon Rekognition
        publishes a completion status to the Amazon Simple Notification Service topic registered in
        the initial call to ``StartlabelDetection`` . To get the results of the label detection
        operation, first check that the status value published to the Amazon SNS topic is
        ``SUCCEEDED`` . If so, call  GetLabelDetection and pass the job identifier (``JobId`` ) from
        the initial call to ``StartLabelDetection`` .

         ``GetLabelDetection`` returns an array of detected labels (``Labels`` ) sorted by the time
         the labels were detected. You can also sort by the label name by specifying ``NAME`` for
         the ``SortBy`` input parameter.

        The labels returned include the label name, the percentage confidence in the accuracy of the
        detected label, and the time the label was detected in the video.

        The returned labels also include bounding box information for common objects, a hierarchical
        taxonomy of detected labels, and the version of the label model used for detection.

        Use MaxResults parameter to limit the number of labels returned. If there are more results
        than specified in ``MaxResults`` , the value of ``NextToken`` in the operation response
        contains a pagination token for getting the next set of results. To get the next page of
        results, call ``GetlabelDetection`` and populate the ``NextToken`` request parameter with
        the token value returned from the previous call to ``GetLabelDetection`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/GetLabelDetection>`_

        **Request Syntax**
        ::

          response = client.get_label_detection(
              JobId='string',
              MaxResults=123,
              NextToken='string',
              SortBy='NAME'|'TIMESTAMP'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]**

          Job identifier for the label detection operation for which you want results returned. You
          get the job identifer from an initial call to ``StartlabelDetection`` .

        :type MaxResults: integer
        :param MaxResults:

          Maximum number of results to return per paginated call. The largest value you can specify
          is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned.
          The default value is 1000.

        :type NextToken: string
        :param NextToken:

          If the previous response was incomplete (because there are more labels to retrieve),
          Amazon Rekognition Video returns a pagination token in the response. You can use this
          pagination token to retrieve the next set of labels.

        :type SortBy: string
        :param SortBy:

          Sort to use for elements in the ``Labels`` array. Use ``TIMESTAMP`` to sort array elements
          by the time labels are detected. Use ``NAME`` to alphabetically group elements for a label
          together. Within each label group, the array element are sorted by detection confidence.
          The default sort is by ``TIMESTAMP`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
                'StatusMessage': 'string',
                'VideoMetadata': {
                    'Codec': 'string',
                    'DurationMillis': 123,
                    'Format': 'string',
                    'FrameRate': ...,
                    'FrameHeight': 123,
                    'FrameWidth': 123
                },
                'NextToken': 'string',
                'Labels': [
                    {
                        'Timestamp': 123,
                        'Label': {
                            'Name': 'string',
                            'Confidence': ...,
                            'Instances': [
                                {
                                    'BoundingBox': {
                                        'Width': ...,
                                        'Height': ...,
                                        'Left': ...,
                                        'Top': ...
                                    },
                                    'Confidence': ...
                                },
                            ],
                            'Parents': [
                                {
                                    'Name': 'string'
                                },
                            ]
                        }
                    },
                ],
                'LabelModelVersion': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **JobStatus** *(string) --*

              The current status of the label detection job.

            - **StatusMessage** *(string) --*

              If the job fails, ``StatusMessage`` provides a descriptive error message.

            - **VideoMetadata** *(dict) --*

              Information about a video that Amazon Rekognition Video analyzed. ``Videometadata`` is
              returned in every page of paginated responses from a Amazon Rekognition video
              operation.

              - **Codec** *(string) --*

                Type of compression used in the analyzed video.

              - **DurationMillis** *(integer) --*

                Length of the video in milliseconds.

              - **Format** *(string) --*

                Format of the analyzed video. Possible values are MP4, MOV and AVI.

              - **FrameRate** *(float) --*

                Number of frames per second in the video.

              - **FrameHeight** *(integer) --*

                Vertical pixel dimension of the video.

              - **FrameWidth** *(integer) --*

                Horizontal pixel dimension of the video.

            - **NextToken** *(string) --*

              If the response is truncated, Amazon Rekognition Video returns this token that you can
              use in the subsequent request to retrieve the next set of labels.

            - **Labels** *(list) --*

              An array of labels detected in the video. Each element contains the detected label and
              the time, in milliseconds from the start of the video, that the label was detected.

              - *(dict) --*

                Information about a label detected in a video analysis request and the time the
                label was detected in the video.

                - **Timestamp** *(integer) --*

                  Time, in milliseconds from the start of the video, that the label was detected.

                - **Label** *(dict) --*

                  Details about the detected label.

                  - **Name** *(string) --*

                    The name (label) of the object or scene.

                  - **Confidence** *(float) --*

                    Level of confidence.

                  - **Instances** *(list) --*

                    If ``Label`` represents an object, ``Instances`` contains the bounding boxes for
                    each instance of the detected object. Bounding boxes are returned for common
                    object labels such as people, cars, furniture, apparel or pets.

                    - *(dict) --*

                      An instance of a label returned by Amazon Rekognition Image ( DetectLabels )
                      or by Amazon Rekognition Video ( GetLabelDetection ).

                      - **BoundingBox** *(dict) --*

                        The position of the label instance on the image.

                        - **Width** *(float) --*

                          Width of the bounding box as a ratio of the overall image width.

                        - **Height** *(float) --*

                          Height of the bounding box as a ratio of the overall image height.

                        - **Left** *(float) --*

                          Left coordinate of the bounding box as a ratio of overall image width.

                        - **Top** *(float) --*

                          Top coordinate of the bounding box as a ratio of overall image height.

                      - **Confidence** *(float) --*

                        The confidence that Amazon Rekognition has in the accuracy of the bounding
                        box.

                  - **Parents** *(list) --*

                    The parent labels for a label. The response includes all ancestor labels.

                    - *(dict) --*

                      A parent label for a label. A label can have 0, 1, or more parents.

                      - **Name** *(string) --*

                        The name of the parent label.

            - **LabelModelVersion** *(string) --*

              Version number of the label detection model that was used to detect labels.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_person_tracking(
        self,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: Literal["INDEX", "TIMESTAMP"] = None,
    ) -> ClientGetPersonTrackingResponseTypeDef:
        """
        Gets the path tracking results of a Amazon Rekognition Video analysis started by
        StartPersonTracking .

        The person path tracking operation is started by a call to ``StartPersonTracking`` which
        returns a job identifier (``JobId`` ). When the operation finishes, Amazon Rekognition Video
        publishes a completion status to the Amazon Simple Notification Service topic registered in
        the initial call to ``StartPersonTracking`` .

        To get the results of the person path tracking operation, first check that the status value
        published to the Amazon SNS topic is ``SUCCEEDED`` . If so, call  GetPersonTracking and pass
        the job identifier (``JobId`` ) from the initial call to ``StartPersonTracking`` .

         ``GetPersonTracking`` returns an array, ``Persons`` , of tracked persons and the time(s)
         their paths were tracked in the video.

        .. note::

           ``GetPersonTracking`` only returns the default facial attributes (``BoundingBox`` ,
           ``Confidence`` , ``Landmarks`` , ``Pose`` , and ``Quality`` ). The other facial
           attributes listed in the ``Face`` object of the following response syntax are not
           returned.

          For more information, see FaceDetail in the Amazon Rekognition Developer Guide.

        By default, the array is sorted by the time(s) a person's path is tracked in the video. You
        can sort by tracked persons by specifying ``INDEX`` for the ``SortBy`` input parameter.

        Use the ``MaxResults`` parameter to limit the number of items returned. If there are more
        results than specified in ``MaxResults`` , the value of ``NextToken`` in the operation
        response contains a pagination token for getting the next set of results. To get the next
        page of results, call ``GetPersonTracking`` and populate the ``NextToken`` request parameter
        with the token value returned from the previous call to ``GetPersonTracking`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/GetPersonTracking>`_

        **Request Syntax**
        ::

          response = client.get_person_tracking(
              JobId='string',
              MaxResults=123,
              NextToken='string',
              SortBy='INDEX'|'TIMESTAMP'
          )
        :type JobId: string
        :param JobId: **[REQUIRED]**

          The identifier for a job that tracks persons in a video. You get the ``JobId`` from a call
          to ``StartPersonTracking`` .

        :type MaxResults: integer
        :param MaxResults:

          Maximum number of results to return per paginated call. The largest value you can specify
          is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned.
          The default value is 1000.

        :type NextToken: string
        :param NextToken:

          If the previous response was incomplete (because there are more persons to retrieve),
          Amazon Rekognition Video returns a pagination token in the response. You can use this
          pagination token to retrieve the next set of persons.

        :type SortBy: string
        :param SortBy:

          Sort to use for elements in the ``Persons`` array. Use ``TIMESTAMP`` to sort array
          elements by the time persons are detected. Use ``INDEX`` to sort by the tracked persons.
          If you sort by ``INDEX`` , the array elements for each person are sorted by detection
          confidence. The default sort is by ``TIMESTAMP`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
                'StatusMessage': 'string',
                'VideoMetadata': {
                    'Codec': 'string',
                    'DurationMillis': 123,
                    'Format': 'string',
                    'FrameRate': ...,
                    'FrameHeight': 123,
                    'FrameWidth': 123
                },
                'NextToken': 'string',
                'Persons': [
                    {
                        'Timestamp': 123,
                        'Person': {
                            'Index': 123,
                            'BoundingBox': {
                                'Width': ...,
                                'Height': ...,
                                'Left': ...,
                                'Top': ...
                            },
                            'Face': {
                                'BoundingBox': {
                                    'Width': ...,
                                    'Height': ...,
                                    'Left': ...,
                                    'Top': ...
                                },
                                'AgeRange': {
                                    'Low': 123,
                                    'High': 123
                                },
                                'Smile': {
                                    'Value': True|False,
                                    'Confidence': ...
                                },
                                'Eyeglasses': {
                                    'Value': True|False,
                                    'Confidence': ...
                                },
                                'Sunglasses': {
                                    'Value': True|False,
                                    'Confidence': ...
                                },
                                'Gender': {
                                    'Value': 'Male'|'Female',
                                    'Confidence': ...
                                },
                                'Beard': {
                                    'Value': True|False,
                                    'Confidence': ...
                                },
                                'Mustache': {
                                    'Value': True|False,
                                    'Confidence': ...
                                },
                                'EyesOpen': {
                                    'Value': True|False,
                                    'Confidence': ...
                                },
                                'MouthOpen': {
                                    'Value': True|False,
                                    'Confidence': ...
                                },
                                'Emotions': [
                                    {
                                        'Type':
                                        'HAPPY'|'SAD'|'ANGRY'
                                        |'CONFUSED'|'DISGUSTED'
                                        |'SURPRISED'|'CALM'
                                        |'UNKNOWN'|'FEAR',
                                        'Confidence': ...
                                    },
                                ],
                                'Landmarks': [
                                    {
                                        'Type':
                                        'eyeLeft'|'eyeRight'|'nose'
                                        |'mouthLeft'|'mouthRight'
                                        |'leftEyeBrowLeft'
                                        |'leftEyeBrowRight'
                                        |'leftEyeBrowUp'
                                        |'rightEyeBrowLeft'
                                        |'rightEyeBrowRight'
                                        |'rightEyeBrowUp'
                                        |'leftEyeLeft'
                                        |'leftEyeRight'|'leftEyeUp'
                                        |'leftEyeDown'
                                        |'rightEyeLeft'
                                        |'rightEyeRight'
                                        |'rightEyeUp'|'rightEyeDown'
                                        |'noseLeft'|'noseRight'
                                        |'mouthUp'|'mouthDown'
                                        |'leftPupil'|'rightPupil'
                                        |'upperJawlineLeft'
                                        |'midJawlineLeft'
                                        |'chinBottom'
                                        |'midJawlineRight'
                                        |'upperJawlineRight',
                                        'X': ...,
                                        'Y': ...
                                    },
                                ],
                                'Pose': {
                                    'Roll': ...,
                                    'Yaw': ...,
                                    'Pitch': ...
                                },
                                'Quality': {
                                    'Brightness': ...,
                                    'Sharpness': ...
                                },
                                'Confidence': ...
                            }
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **JobStatus** *(string) --*

              The current status of the person tracking job.

            - **StatusMessage** *(string) --*

              If the job fails, ``StatusMessage`` provides a descriptive error message.

            - **VideoMetadata** *(dict) --*

              Information about a video that Amazon Rekognition Video analyzed. ``Videometadata`` is
              returned in every page of paginated responses from a Amazon Rekognition Video
              operation.

              - **Codec** *(string) --*

                Type of compression used in the analyzed video.

              - **DurationMillis** *(integer) --*

                Length of the video in milliseconds.

              - **Format** *(string) --*

                Format of the analyzed video. Possible values are MP4, MOV and AVI.

              - **FrameRate** *(float) --*

                Number of frames per second in the video.

              - **FrameHeight** *(integer) --*

                Vertical pixel dimension of the video.

              - **FrameWidth** *(integer) --*

                Horizontal pixel dimension of the video.

            - **NextToken** *(string) --*

              If the response is truncated, Amazon Rekognition Video returns this token that you can
              use in the subsequent request to retrieve the next set of persons.

            - **Persons** *(list) --*

              An array of the persons detected in the video and the time(s) their path was tracked
              throughout the video. An array element will exist for each time a person's path is
              tracked.

              - *(dict) --*

                Details and path tracking information for a single time a person's path is tracked
                in a video. Amazon Rekognition operations that track people's paths return an array
                of ``PersonDetection`` objects with elements for each time a person's path is
                tracked in a video.

                For more information, see GetPersonTracking in the Amazon Rekognition Developer
                Guide.

                - **Timestamp** *(integer) --*

                  The time, in milliseconds from the start of the video, that the person's path was
                  tracked.

                - **Person** *(dict) --*

                  Details about a person whose path was tracked in a video.

                  - **Index** *(integer) --*

                    Identifier for the person detected person within a video. Use to keep track of
                    the person throughout the video. The identifier is not stored by Amazon
                    Rekognition.

                  - **BoundingBox** *(dict) --*

                    Bounding box around the detected person.

                    - **Width** *(float) --*

                      Width of the bounding box as a ratio of the overall image width.

                    - **Height** *(float) --*

                      Height of the bounding box as a ratio of the overall image height.

                    - **Left** *(float) --*

                      Left coordinate of the bounding box as a ratio of overall image width.

                    - **Top** *(float) --*

                      Top coordinate of the bounding box as a ratio of overall image height.

                  - **Face** *(dict) --*

                    Face details for the detected person.

                    - **BoundingBox** *(dict) --*

                      Bounding box of the face. Default attribute.

                      - **Width** *(float) --*

                        Width of the bounding box as a ratio of the overall image width.

                      - **Height** *(float) --*

                        Height of the bounding box as a ratio of the overall image height.

                      - **Left** *(float) --*

                        Left coordinate of the bounding box as a ratio of overall image width.

                      - **Top** *(float) --*

                        Top coordinate of the bounding box as a ratio of overall image height.

                    - **AgeRange** *(dict) --*

                      The estimated age range, in years, for the face. Low represents the lowest
                      estimated age and High represents the highest estimated age.

                      - **Low** *(integer) --*

                        The lowest estimated age.

                      - **High** *(integer) --*

                        The highest estimated age.

                    - **Smile** *(dict) --*

                      Indicates whether or not the face is smiling, and the confidence level in the
                      determination.

                      - **Value** *(boolean) --*

                        Boolean value that indicates whether the face is smiling or not.

                      - **Confidence** *(float) --*

                        Level of confidence in the determination.

                    - **Eyeglasses** *(dict) --*

                      Indicates whether or not the face is wearing eye glasses, and the confidence
                      level in the determination.

                      - **Value** *(boolean) --*

                        Boolean value that indicates whether the face is wearing eye glasses or not.

                      - **Confidence** *(float) --*

                        Level of confidence in the determination.

                    - **Sunglasses** *(dict) --*

                      Indicates whether or not the face is wearing sunglasses, and the confidence
                      level in the determination.

                      - **Value** *(boolean) --*

                        Boolean value that indicates whether the face is wearing sunglasses or not.

                      - **Confidence** *(float) --*

                        Level of confidence in the determination.

                    - **Gender** *(dict) --*

                      The predicted gender of a detected face.

                      - **Value** *(string) --*

                        The predicted gender of the face.

                      - **Confidence** *(float) --*

                        Level of confidence in the prediction.

                    - **Beard** *(dict) --*

                      Indicates whether or not the face has a beard, and the confidence level in the
                      determination.

                      - **Value** *(boolean) --*

                        Boolean value that indicates whether the face has beard or not.

                      - **Confidence** *(float) --*

                        Level of confidence in the determination.

                    - **Mustache** *(dict) --*

                      Indicates whether or not the face has a mustache, and the confidence level in
                      the determination.

                      - **Value** *(boolean) --*

                        Boolean value that indicates whether the face has mustache or not.

                      - **Confidence** *(float) --*

                        Level of confidence in the determination.

                    - **EyesOpen** *(dict) --*

                      Indicates whether or not the eyes on the face are open, and the confidence
                      level in the determination.

                      - **Value** *(boolean) --*

                        Boolean value that indicates whether the eyes on the face are open.

                      - **Confidence** *(float) --*

                        Level of confidence in the determination.

                    - **MouthOpen** *(dict) --*

                      Indicates whether or not the mouth on the face is open, and the confidence
                      level in the determination.

                      - **Value** *(boolean) --*

                        Boolean value that indicates whether the mouth on the face is open or not.

                      - **Confidence** *(float) --*

                        Level of confidence in the determination.

                    - **Emotions** *(list) --*

                      The emotions that appear to be expressed on the face, and the confidence level
                      in the determination. The API is only making a determination of the physical
                      appearance of a person's face. It is not a determination of the person’s
                      internal emotional state and should not be used in such a way. For example, a
                      person pretending to have a sad face might not be sad emotionally.

                      - *(dict) --*

                        The emotions that appear to be expressed on the face, and the confidence
                        level in the determination. The API is only making a determination of the
                        physical appearance of a person's face. It is not a determination of the
                        person’s internal emotional state and should not be used in such a way. For
                        example, a person pretending to have a sad face might not be sad
                        emotionally.

                        - **Type** *(string) --*

                          Type of emotion detected.

                        - **Confidence** *(float) --*

                          Level of confidence in the determination.

                    - **Landmarks** *(list) --*

                      Indicates the location of landmarks on the face. Default attribute.

                      - *(dict) --*

                        Indicates the location of the landmark on the face.

                        - **Type** *(string) --*

                          Type of landmark.

                        - **X** *(float) --*

                          The x-coordinate from the top left of the landmark expressed as the ratio
                          of the width of the image. For example, if the image is 700 x 200 and the
                          x-coordinate of the landmark is at 350 pixels, this value is 0.5.

                        - **Y** *(float) --*

                          The y-coordinate from the top left of the landmark expressed as the ratio
                          of the height of the image. For example, if the image is 700 x 200 and the
                          y-coordinate of the landmark is at 100 pixels, this value is 0.5.

                    - **Pose** *(dict) --*

                      Indicates the pose of the face as determined by its pitch, roll, and yaw.
                      Default attribute.

                      - **Roll** *(float) --*

                        Value representing the face rotation on the roll axis.

                      - **Yaw** *(float) --*

                        Value representing the face rotation on the yaw axis.

                      - **Pitch** *(float) --*

                        Value representing the face rotation on the pitch axis.

                    - **Quality** *(dict) --*

                      Identifies image brightness and sharpness. Default attribute.

                      - **Brightness** *(float) --*

                        Value representing brightness of the face. The service returns a value
                        between 0 and 100 (inclusive). A higher value indicates a brighter face
                        image.

                      - **Sharpness** *(float) --*

                        Value representing sharpness of the face. The service returns a value
                        between 0 and 100 (inclusive). A higher value indicates a sharper face
                        image.

                    - **Confidence** *(float) --*

                      Confidence level that the bounding box contains a face (and not a different
                      object such as a tree). Default attribute.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def index_faces(
        self,
        CollectionId: str,
        Image: ClientIndexFacesImageTypeDef,
        ExternalImageId: str = None,
        DetectionAttributes: List[Literal["DEFAULT", "ALL"]] = None,
        MaxFaces: int = None,
        QualityFilter: Literal["NONE", "AUTO", "LOW", "MEDIUM", "HIGH"] = None,
    ) -> ClientIndexFacesResponseTypeDef:
        """
        Detects faces in the input image and adds them to the specified collection.

        Amazon Rekognition doesn't save the actual faces that are detected. Instead, the underlying
        detection algorithm first detects the faces in the input image. For each face, the algorithm
        extracts facial features into a feature vector, and stores it in the backend database.
        Amazon Rekognition uses feature vectors when it performs face match and search operations
        using the  SearchFaces and  SearchFacesByImage operations.

        For more information, see Adding Faces to a Collection in the Amazon Rekognition Developer
        Guide.

        To get the number of faces in a collection, call  DescribeCollection .

        If you're using version 1.0 of the face detection model, ``IndexFaces`` indexes the 15
        largest faces in the input image. Later versions of the face detection model index the 100
        largest faces in the input image.

        If you're using version 4 or later of the face model, image orientation information is not
        returned in the ``OrientationCorrection`` field.

        To determine which version of the model you're using, call  DescribeCollection and supply
        the collection ID. You can also get the model version from the value of ``FaceModelVersion``
        in the response from ``IndexFaces``

        For more information, see Model Versioning in the Amazon Rekognition Developer Guide.

        If you provide the optional ``ExternalImageID`` for the input image you provided, Amazon
        Rekognition associates this ID with all faces that it detects. When you call the  ListFaces
        operation, the response returns the external ID. You can use this external image ID to
        create a client-side index to associate the faces with each image. You can then use the
        index to find all faces in an image.

        You can specify the maximum number of faces to index with the ``MaxFaces`` input parameter.
        This is useful when you want to index the largest faces in an image and don't want to index
        smaller faces, such as those belonging to people standing in the background.

        The ``QualityFilter`` input parameter allows you to filter out detected faces that don’t
        meet a required quality bar. The quality bar is based on a variety of common use cases. By
        default, ``IndexFaces`` chooses the quality bar that's used to filter faces. You can also
        explicitly choose the quality bar. Use ``QualityFilter`` , to set the quality bar by
        specifying ``LOW`` , ``MEDIUM`` , or ``HIGH`` . If you do not want to filter detected faces,
        specify ``NONE`` .

        .. note::

          To use quality filtering, you need a collection associated with version 3 of the face
          model or higher. To get the version of the face model associated with a collection, call
          DescribeCollection .

        Information about faces detected in an image, but not indexed, is returned in an array of
        UnindexedFace objects, ``UnindexedFaces`` . Faces aren't indexed for reasons such as:

        * The number of faces detected exceeds the value of the ``MaxFaces`` request parameter.

        * The face is too small compared to the image dimensions.

        * The face is too blurry.

        * The image is too dark.

        * The face has an extreme pose.

        * The face doesn’t have enough detail to be suitable for face search.

        In response, the ``IndexFaces`` operation returns an array of metadata for all detected
        faces, ``FaceRecords`` . This includes:

        * The bounding box, ``BoundingBox`` , of the detected face.

        * A confidence value, ``Confidence`` , which indicates the confidence that the bounding box
        contains a face.

        * A face ID, ``FaceId`` , assigned by the service for each face that's detected and stored.

        * An image ID, ``ImageId`` , assigned by the service for the input image.

        If you request all facial attributes (by using the ``detectionAttributes`` parameter),
        Amazon Rekognition returns detailed facial attributes, such as facial landmarks (for
        example, location of eye and mouth) and other facial attributes. If you provide the same
        image, specify the same collection, and use the same external ID in the ``IndexFaces``
        operation, Amazon Rekognition doesn't save duplicate face metadata.

        The input image is passed either as base64-encoded image bytes, or as a reference to an
        image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations,
        passing image bytes isn't supported. The image must be formatted as a PNG or JPEG file.

        This operation requires permissions to perform the ``rekognition:IndexFaces`` action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/IndexFaces>`_

        **Request Syntax**
        ::

          response = client.index_faces(
              CollectionId='string',
              Image={
                  'Bytes': b'bytes',
                  'S3Object': {
                      'Bucket': 'string',
                      'Name': 'string',
                      'Version': 'string'
                  }
              },
              ExternalImageId='string',
              DetectionAttributes=[
                  'DEFAULT'|'ALL',
              ],
              MaxFaces=123,
              QualityFilter='NONE'|'AUTO'|'LOW'|'MEDIUM'|'HIGH'
          )
        :type CollectionId: string
        :param CollectionId: **[REQUIRED]**

          The ID of an existing collection to which you want to add the faces that are detected in
          the input images.

        :type Image: dict
        :param Image: **[REQUIRED]**

          The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call
          Amazon Rekognition operations, passing base64-encoded image bytes isn't supported.

          If you are using an AWS SDK to call Amazon Rekognition, you might not need to
          base64-encode image bytes passed using the ``Bytes`` field. For more information, see
          Images in the Amazon Rekognition developer guide.

          - **Bytes** *(bytes) --*

            Blob of image bytes up to 5 MBs.

          - **S3Object** *(dict) --*

            Identifies an S3 object as the image source.

            - **Bucket** *(string) --*

              Name of the S3 bucket.

            - **Name** *(string) --*

              S3 object key name.

            - **Version** *(string) --*

              If the bucket is versioning enabled, you can specify the object version.

        :type ExternalImageId: string
        :param ExternalImageId:

          The ID you want to assign to all the faces detected in the image.

        :type DetectionAttributes: list
        :param DetectionAttributes:

          An array of facial attributes that you want to be returned. This can be the default list
          of attributes or all attributes. If you don't specify a value for ``Attributes`` or if you
          specify ``["DEFAULT"]`` , the API returns the following subset of facial attributes:
          ``BoundingBox`` , ``Confidence`` , ``Pose`` , ``Quality`` , and ``Landmarks`` . If you
          provide ``["ALL"]`` , all facial attributes are returned, but the operation takes longer
          to complete.

          If you provide both, ``["ALL", "DEFAULT"]`` , the service uses a logical AND operator to
          determine which attributes to return (in this case, all attributes).

          - *(string) --*

        :type MaxFaces: integer
        :param MaxFaces:

          The maximum number of faces to index. The value of ``MaxFaces`` must be greater than or
          equal to 1. ``IndexFaces`` returns no more than 100 detected faces in an image, even if
          you specify a larger value for ``MaxFaces`` .

          If ``IndexFaces`` detects more faces than the value of ``MaxFaces`` , the faces with the
          lowest quality are filtered out first. If there are still more faces than the value of
          ``MaxFaces`` , the faces with the smallest bounding boxes are filtered out (up to the
          number that's needed to satisfy the value of ``MaxFaces`` ). Information about the
          unindexed faces is available in the ``UnindexedFaces`` array.

          The faces that are returned by ``IndexFaces`` are sorted by the largest face bounding box
          size to the smallest size, in descending order.

           ``MaxFaces`` can be used with a collection associated with any version of the face model.

        :type QualityFilter: string
        :param QualityFilter:

          A filter that specifies a quality bar for how much filtering is done to identify faces.
          Filtered faces aren't indexed. If you specify ``AUTO`` , Amazon Rekognition chooses the
          quality bar. If you specify ``LOW`` , ``MEDIUM`` , or ``HIGH`` , filtering removes all
          faces that don’t meet the chosen quality bar. The default value is ``AUTO`` . The quality
          bar is based on a variety of common use cases. Low-quality detections can occur for a
          number of reasons. Some examples are an object that's misidentified as a face, a face
          that's too blurry, or a face with a pose that's too extreme to use. If you specify
          ``NONE`` , no filtering is performed.

          To use quality filtering, the collection you are using must be associated with version 3
          of the face model or higher.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FaceRecords': [
                    {
                        'Face': {
                            'FaceId': 'string',
                            'BoundingBox': {
                                'Width': ...,
                                'Height': ...,
                                'Left': ...,
                                'Top': ...
                            },
                            'ImageId': 'string',
                            'ExternalImageId': 'string',
                            'Confidence': ...
                        },
                        'FaceDetail': {
                            'BoundingBox': {
                                'Width': ...,
                                'Height': ...,
                                'Left': ...,
                                'Top': ...
                            },
                            'AgeRange': {
                                'Low': 123,
                                'High': 123
                            },
                            'Smile': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Eyeglasses': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Sunglasses': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Gender': {
                                'Value': 'Male'|'Female',
                                'Confidence': ...
                            },
                            'Beard': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Mustache': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'EyesOpen': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'MouthOpen': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Emotions': [
                                {
                                    'Type':
                                    'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'
                                    |'DISGUSTED'|'SURPRISED'|'CALM'
                                    |'UNKNOWN'|'FEAR',
                                    'Confidence': ...
                                },
                            ],
                            'Landmarks': [
                                {
                                    'Type':
                                    'eyeLeft'|'eyeRight'|'nose'
                                    |'mouthLeft'|'mouthRight'
                                    |'leftEyeBrowLeft'
                                    |'leftEyeBrowRight'|'leftEyeBrowUp'
                                    |'rightEyeBrowLeft'
                                    |'rightEyeBrowRight'
                                    |'rightEyeBrowUp'|'leftEyeLeft'
                                    |'leftEyeRight'|'leftEyeUp'
                                    |'leftEyeDown'|'rightEyeLeft'
                                    |'rightEyeRight'|'rightEyeUp'
                                    |'rightEyeDown'|'noseLeft'
                                    |'noseRight'|'mouthUp'|'mouthDown'
                                    |'leftPupil'|'rightPupil'
                                    |'upperJawlineLeft'|'midJawlineLeft'
                                    |'chinBottom'|'midJawlineRight'
                                    |'upperJawlineRight',
                                    'X': ...,
                                    'Y': ...
                                },
                            ],
                            'Pose': {
                                'Roll': ...,
                                'Yaw': ...,
                                'Pitch': ...
                            },
                            'Quality': {
                                'Brightness': ...,
                                'Sharpness': ...
                            },
                            'Confidence': ...
                        }
                    },
                ],
                'OrientationCorrection': 'ROTATE_0'|'ROTATE_90'|'ROTATE_180'|'ROTATE_270',
                'FaceModelVersion': 'string',
                'UnindexedFaces': [
                    {
                        'Reasons': [
                            'EXCEEDS_MAX_FACES'|'EXTREME_POSE'|'LOW_BRIGHTNESS'|'LOW_SHARPNESS'
                            |'LOW_CONFIDENCE'|'SMALL_BOUNDING_BOX'|'LOW_FACE_QUALITY',
                        ],
                        'FaceDetail': {
                            'BoundingBox': {
                                'Width': ...,
                                'Height': ...,
                                'Left': ...,
                                'Top': ...
                            },
                            'AgeRange': {
                                'Low': 123,
                                'High': 123
                            },
                            'Smile': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Eyeglasses': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Sunglasses': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Gender': {
                                'Value': 'Male'|'Female',
                                'Confidence': ...
                            },
                            'Beard': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Mustache': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'EyesOpen': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'MouthOpen': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Emotions': [
                                {
                                    'Type':
                                    'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'
                                    |'DISGUSTED'|'SURPRISED'|'CALM'
                                    |'UNKNOWN'|'FEAR',
                                    'Confidence': ...
                                },
                            ],
                            'Landmarks': [
                                {
                                    'Type':
                                    'eyeLeft'|'eyeRight'|'nose'
                                    |'mouthLeft'|'mouthRight'
                                    |'leftEyeBrowLeft'
                                    |'leftEyeBrowRight'|'leftEyeBrowUp'
                                    |'rightEyeBrowLeft'
                                    |'rightEyeBrowRight'
                                    |'rightEyeBrowUp'|'leftEyeLeft'
                                    |'leftEyeRight'|'leftEyeUp'
                                    |'leftEyeDown'|'rightEyeLeft'
                                    |'rightEyeRight'|'rightEyeUp'
                                    |'rightEyeDown'|'noseLeft'
                                    |'noseRight'|'mouthUp'|'mouthDown'
                                    |'leftPupil'|'rightPupil'
                                    |'upperJawlineLeft'|'midJawlineLeft'
                                    |'chinBottom'|'midJawlineRight'
                                    |'upperJawlineRight',
                                    'X': ...,
                                    'Y': ...
                                },
                            ],
                            'Pose': {
                                'Roll': ...,
                                'Yaw': ...,
                                'Pitch': ...
                            },
                            'Quality': {
                                'Brightness': ...,
                                'Sharpness': ...
                            },
                            'Confidence': ...
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **FaceRecords** *(list) --*

              An array of faces detected and added to the collection. For more information, see
              Searching Faces in a Collection in the Amazon Rekognition Developer Guide.

              - *(dict) --*

                Object containing both the face metadata (stored in the backend database), and
                facial attributes that are detected but aren't stored in the database.

                - **Face** *(dict) --*

                  Describes the face properties such as the bounding box, face ID, image ID of the
                  input image, and external image ID that you assigned.

                  - **FaceId** *(string) --*

                    Unique identifier that Amazon Rekognition assigns to the face.

                  - **BoundingBox** *(dict) --*

                    Bounding box of the face.

                    - **Width** *(float) --*

                      Width of the bounding box as a ratio of the overall image width.

                    - **Height** *(float) --*

                      Height of the bounding box as a ratio of the overall image height.

                    - **Left** *(float) --*

                      Left coordinate of the bounding box as a ratio of overall image width.

                    - **Top** *(float) --*

                      Top coordinate of the bounding box as a ratio of overall image height.

                  - **ImageId** *(string) --*

                    Unique identifier that Amazon Rekognition assigns to the input image.

                  - **ExternalImageId** *(string) --*

                    Identifier that you assign to all the faces in the input image.

                  - **Confidence** *(float) --*

                    Confidence level that the bounding box contains a face (and not a different
                    object such as a tree).

                - **FaceDetail** *(dict) --*

                  Structure containing attributes of the face that the algorithm detected.

                  - **BoundingBox** *(dict) --*

                    Bounding box of the face. Default attribute.

                    - **Width** *(float) --*

                      Width of the bounding box as a ratio of the overall image width.

                    - **Height** *(float) --*

                      Height of the bounding box as a ratio of the overall image height.

                    - **Left** *(float) --*

                      Left coordinate of the bounding box as a ratio of overall image width.

                    - **Top** *(float) --*

                      Top coordinate of the bounding box as a ratio of overall image height.

                  - **AgeRange** *(dict) --*

                    The estimated age range, in years, for the face. Low represents the lowest
                    estimated age and High represents the highest estimated age.

                    - **Low** *(integer) --*

                      The lowest estimated age.

                    - **High** *(integer) --*

                      The highest estimated age.

                  - **Smile** *(dict) --*

                    Indicates whether or not the face is smiling, and the confidence level in the
                    determination.

                    - **Value** *(boolean) --*

                      Boolean value that indicates whether the face is smiling or not.

                    - **Confidence** *(float) --*

                      Level of confidence in the determination.

                  - **Eyeglasses** *(dict) --*

                    Indicates whether or not the face is wearing eye glasses, and the confidence
                    level in the determination.

                    - **Value** *(boolean) --*

                      Boolean value that indicates whether the face is wearing eye glasses or not.

                    - **Confidence** *(float) --*

                      Level of confidence in the determination.

                  - **Sunglasses** *(dict) --*

                    Indicates whether or not the face is wearing sunglasses, and the confidence
                    level in the determination.

                    - **Value** *(boolean) --*

                      Boolean value that indicates whether the face is wearing sunglasses or not.

                    - **Confidence** *(float) --*

                      Level of confidence in the determination.

                  - **Gender** *(dict) --*

                    The predicted gender of a detected face.

                    - **Value** *(string) --*

                      The predicted gender of the face.

                    - **Confidence** *(float) --*

                      Level of confidence in the prediction.

                  - **Beard** *(dict) --*

                    Indicates whether or not the face has a beard, and the confidence level in the
                    determination.

                    - **Value** *(boolean) --*

                      Boolean value that indicates whether the face has beard or not.

                    - **Confidence** *(float) --*

                      Level of confidence in the determination.

                  - **Mustache** *(dict) --*

                    Indicates whether or not the face has a mustache, and the confidence level in
                    the determination.

                    - **Value** *(boolean) --*

                      Boolean value that indicates whether the face has mustache or not.

                    - **Confidence** *(float) --*

                      Level of confidence in the determination.

                  - **EyesOpen** *(dict) --*

                    Indicates whether or not the eyes on the face are open, and the confidence level
                    in the determination.

                    - **Value** *(boolean) --*

                      Boolean value that indicates whether the eyes on the face are open.

                    - **Confidence** *(float) --*

                      Level of confidence in the determination.

                  - **MouthOpen** *(dict) --*

                    Indicates whether or not the mouth on the face is open, and the confidence level
                    in the determination.

                    - **Value** *(boolean) --*

                      Boolean value that indicates whether the mouth on the face is open or not.

                    - **Confidence** *(float) --*

                      Level of confidence in the determination.

                  - **Emotions** *(list) --*

                    The emotions that appear to be expressed on the face, and the confidence level
                    in the determination. The API is only making a determination of the physical
                    appearance of a person's face. It is not a determination of the person’s
                    internal emotional state and should not be used in such a way. For example, a
                    person pretending to have a sad face might not be sad emotionally.

                    - *(dict) --*

                      The emotions that appear to be expressed on the face, and the confidence level
                      in the determination. The API is only making a determination of the physical
                      appearance of a person's face. It is not a determination of the person’s
                      internal emotional state and should not be used in such a way. For example, a
                      person pretending to have a sad face might not be sad emotionally.

                      - **Type** *(string) --*

                        Type of emotion detected.

                      - **Confidence** *(float) --*

                        Level of confidence in the determination.

                  - **Landmarks** *(list) --*

                    Indicates the location of landmarks on the face. Default attribute.

                    - *(dict) --*

                      Indicates the location of the landmark on the face.

                      - **Type** *(string) --*

                        Type of landmark.

                      - **X** *(float) --*

                        The x-coordinate from the top left of the landmark expressed as the ratio of
                        the width of the image. For example, if the image is 700 x 200 and the
                        x-coordinate of the landmark is at 350 pixels, this value is 0.5.

                      - **Y** *(float) --*

                        The y-coordinate from the top left of the landmark expressed as the ratio of
                        the height of the image. For example, if the image is 700 x 200 and the
                        y-coordinate of the landmark is at 100 pixels, this value is 0.5.

                  - **Pose** *(dict) --*

                    Indicates the pose of the face as determined by its pitch, roll, and yaw.
                    Default attribute.

                    - **Roll** *(float) --*

                      Value representing the face rotation on the roll axis.

                    - **Yaw** *(float) --*

                      Value representing the face rotation on the yaw axis.

                    - **Pitch** *(float) --*

                      Value representing the face rotation on the pitch axis.

                  - **Quality** *(dict) --*

                    Identifies image brightness and sharpness. Default attribute.

                    - **Brightness** *(float) --*

                      Value representing brightness of the face. The service returns a value between
                      0 and 100 (inclusive). A higher value indicates a brighter face image.

                    - **Sharpness** *(float) --*

                      Value representing sharpness of the face. The service returns a value between
                      0 and 100 (inclusive). A higher value indicates a sharper face image.

                  - **Confidence** *(float) --*

                    Confidence level that the bounding box contains a face (and not a different
                    object such as a tree). Default attribute.

            - **OrientationCorrection** *(string) --*

              If your collection is associated with a face detection model that's later than version
              3.0, the value of ``OrientationCorrection`` is always null and no orientation
              information is returned.

              If your collection is associated with a face detection model that's version 3.0 or
              earlier, the following applies:

              * If the input image is in .jpeg format, it might contain exchangeable image file
              format (Exif) metadata that includes the image's orientation. Amazon Rekognition uses
              this orientation information to perform image correction - the bounding box
              coordinates are translated to represent object locations after the orientation
              information in the Exif metadata is used to correct the image orientation. Images in
              .png format don't contain Exif metadata. The value of ``OrientationCorrection`` is
              null.

              * If the image doesn't contain orientation information in its Exif metadata, Amazon
              Rekognition returns an estimated orientation (ROTATE_0, ROTATE_90, ROTATE_180,
              ROTATE_270). Amazon Rekognition doesn’t perform image correction for images. The
              bounding box coordinates aren't translated and represent the object locations before
              the image is rotated.

              Bounding box information is returned in the ``FaceRecords`` array. You can get the
              version of the face detection model by calling  DescribeCollection .

            - **FaceModelVersion** *(string) --*

              The version number of the face detection model that's associated with the input
              collection (``CollectionId`` ).

            - **UnindexedFaces** *(list) --*

              An array of faces that were detected in the image but weren't indexed. They weren't
              indexed because the quality filter identified them as low quality, or the ``MaxFaces``
              request parameter filtered them out. To use the quality filter, you specify the
              ``QualityFilter`` request parameter.

              - *(dict) --*

                A face that  IndexFaces detected, but didn't index. Use the ``Reasons`` response
                attribute to determine why a face wasn't indexed.

                - **Reasons** *(list) --*

                  An array of reasons that specify why a face wasn't indexed.

                  * EXTREME_POSE - The face is at a pose that can't be detected. For example, the
                  head is turned too far away from the camera.

                  * EXCEEDS_MAX_FACES - The number of faces detected is already higher than that
                  specified by the ``MaxFaces`` input parameter for ``IndexFaces`` .

                  * LOW_BRIGHTNESS - The image is too dark.

                  * LOW_SHARPNESS - The image is too blurry.

                  * LOW_CONFIDENCE - The face was detected with a low confidence.

                  * SMALL_BOUNDING_BOX - The bounding box around the face is too small.

                  - *(string) --*

                - **FaceDetail** *(dict) --*

                  The structure that contains attributes of a face that ``IndexFaces`` detected, but
                  didn't index.

                  - **BoundingBox** *(dict) --*

                    Bounding box of the face. Default attribute.

                    - **Width** *(float) --*

                      Width of the bounding box as a ratio of the overall image width.

                    - **Height** *(float) --*

                      Height of the bounding box as a ratio of the overall image height.

                    - **Left** *(float) --*

                      Left coordinate of the bounding box as a ratio of overall image width.

                    - **Top** *(float) --*

                      Top coordinate of the bounding box as a ratio of overall image height.

                  - **AgeRange** *(dict) --*

                    The estimated age range, in years, for the face. Low represents the lowest
                    estimated age and High represents the highest estimated age.

                    - **Low** *(integer) --*

                      The lowest estimated age.

                    - **High** *(integer) --*

                      The highest estimated age.

                  - **Smile** *(dict) --*

                    Indicates whether or not the face is smiling, and the confidence level in the
                    determination.

                    - **Value** *(boolean) --*

                      Boolean value that indicates whether the face is smiling or not.

                    - **Confidence** *(float) --*

                      Level of confidence in the determination.

                  - **Eyeglasses** *(dict) --*

                    Indicates whether or not the face is wearing eye glasses, and the confidence
                    level in the determination.

                    - **Value** *(boolean) --*

                      Boolean value that indicates whether the face is wearing eye glasses or not.

                    - **Confidence** *(float) --*

                      Level of confidence in the determination.

                  - **Sunglasses** *(dict) --*

                    Indicates whether or not the face is wearing sunglasses, and the confidence
                    level in the determination.

                    - **Value** *(boolean) --*

                      Boolean value that indicates whether the face is wearing sunglasses or not.

                    - **Confidence** *(float) --*

                      Level of confidence in the determination.

                  - **Gender** *(dict) --*

                    The predicted gender of a detected face.

                    - **Value** *(string) --*

                      The predicted gender of the face.

                    - **Confidence** *(float) --*

                      Level of confidence in the prediction.

                  - **Beard** *(dict) --*

                    Indicates whether or not the face has a beard, and the confidence level in the
                    determination.

                    - **Value** *(boolean) --*

                      Boolean value that indicates whether the face has beard or not.

                    - **Confidence** *(float) --*

                      Level of confidence in the determination.

                  - **Mustache** *(dict) --*

                    Indicates whether or not the face has a mustache, and the confidence level in
                    the determination.

                    - **Value** *(boolean) --*

                      Boolean value that indicates whether the face has mustache or not.

                    - **Confidence** *(float) --*

                      Level of confidence in the determination.

                  - **EyesOpen** *(dict) --*

                    Indicates whether or not the eyes on the face are open, and the confidence level
                    in the determination.

                    - **Value** *(boolean) --*

                      Boolean value that indicates whether the eyes on the face are open.

                    - **Confidence** *(float) --*

                      Level of confidence in the determination.

                  - **MouthOpen** *(dict) --*

                    Indicates whether or not the mouth on the face is open, and the confidence level
                    in the determination.

                    - **Value** *(boolean) --*

                      Boolean value that indicates whether the mouth on the face is open or not.

                    - **Confidence** *(float) --*

                      Level of confidence in the determination.

                  - **Emotions** *(list) --*

                    The emotions that appear to be expressed on the face, and the confidence level
                    in the determination. The API is only making a determination of the physical
                    appearance of a person's face. It is not a determination of the person’s
                    internal emotional state and should not be used in such a way. For example, a
                    person pretending to have a sad face might not be sad emotionally.

                    - *(dict) --*

                      The emotions that appear to be expressed on the face, and the confidence level
                      in the determination. The API is only making a determination of the physical
                      appearance of a person's face. It is not a determination of the person’s
                      internal emotional state and should not be used in such a way. For example, a
                      person pretending to have a sad face might not be sad emotionally.

                      - **Type** *(string) --*

                        Type of emotion detected.

                      - **Confidence** *(float) --*

                        Level of confidence in the determination.

                  - **Landmarks** *(list) --*

                    Indicates the location of landmarks on the face. Default attribute.

                    - *(dict) --*

                      Indicates the location of the landmark on the face.

                      - **Type** *(string) --*

                        Type of landmark.

                      - **X** *(float) --*

                        The x-coordinate from the top left of the landmark expressed as the ratio of
                        the width of the image. For example, if the image is 700 x 200 and the
                        x-coordinate of the landmark is at 350 pixels, this value is 0.5.

                      - **Y** *(float) --*

                        The y-coordinate from the top left of the landmark expressed as the ratio of
                        the height of the image. For example, if the image is 700 x 200 and the
                        y-coordinate of the landmark is at 100 pixels, this value is 0.5.

                  - **Pose** *(dict) --*

                    Indicates the pose of the face as determined by its pitch, roll, and yaw.
                    Default attribute.

                    - **Roll** *(float) --*

                      Value representing the face rotation on the roll axis.

                    - **Yaw** *(float) --*

                      Value representing the face rotation on the yaw axis.

                    - **Pitch** *(float) --*

                      Value representing the face rotation on the pitch axis.

                  - **Quality** *(dict) --*

                    Identifies image brightness and sharpness. Default attribute.

                    - **Brightness** *(float) --*

                      Value representing brightness of the face. The service returns a value between
                      0 and 100 (inclusive). A higher value indicates a brighter face image.

                    - **Sharpness** *(float) --*

                      Value representing sharpness of the face. The service returns a value between
                      0 and 100 (inclusive). A higher value indicates a sharper face image.

                  - **Confidence** *(float) --*

                    Confidence level that the bounding box contains a face (and not a different
                    object such as a tree). Default attribute.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_collections(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListCollectionsResponseTypeDef:
        """
        Returns list of collection IDs in your account. If the result is truncated, the response
        also provides a ``NextToken`` that you can use in the subsequent request to fetch the next
        set of collection IDs.

        For an example, see Listing Collections in the Amazon Rekognition Developer Guide.

        This operation requires permissions to perform the ``rekognition:ListCollections`` action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/ListCollections>`_

        **Request Syntax**
        ::

          response = client.list_collections(
              NextToken='string',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken:

          Pagination token from the previous response.

        :type MaxResults: integer
        :param MaxResults:

          Maximum number of collection IDs to return.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CollectionIds': [
                    'string',
                ],
                'NextToken': 'string',
                'FaceModelVersions': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **CollectionIds** *(list) --*

              An array of collection IDs.

              - *(string) --*

            - **NextToken** *(string) --*

              If the result is truncated, the response provides a ``NextToken`` that you can use in
              the subsequent request to fetch the next set of collection IDs.

            - **FaceModelVersions** *(list) --*

              Version numbers of the face detection models associated with the collections in the
              array ``CollectionIds`` . For example, the value of ``FaceModelVersions[2]`` is the
              version number for the face detection model used by the collection in
              ``CollectionId[2]`` .

              - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_faces(
        self, CollectionId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListFacesResponseTypeDef:
        """
        Returns metadata for faces in the specified collection. This metadata includes information
        such as the bounding box coordinates, the confidence (that the bounding box contains a
        face), and face ID. For an example, see Listing Faces in a Collection in the Amazon
        Rekognition Developer Guide.

        This operation requires permissions to perform the ``rekognition:ListFaces`` action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/ListFaces>`_

        **Request Syntax**
        ::

          response = client.list_faces(
              CollectionId='string',
              NextToken='string',
              MaxResults=123
          )
        :type CollectionId: string
        :param CollectionId: **[REQUIRED]**

          ID of the collection from which to list the faces.

        :type NextToken: string
        :param NextToken:

          If the previous response was incomplete (because there is more data to retrieve), Amazon
          Rekognition returns a pagination token in the response. You can use this pagination token
          to retrieve the next set of faces.

        :type MaxResults: integer
        :param MaxResults:

          Maximum number of faces to return.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Faces': [
                    {
                        'FaceId': 'string',
                        'BoundingBox': {
                            'Width': ...,
                            'Height': ...,
                            'Left': ...,
                            'Top': ...
                        },
                        'ImageId': 'string',
                        'ExternalImageId': 'string',
                        'Confidence': ...
                    },
                ],
                'NextToken': 'string',
                'FaceModelVersion': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Faces** *(list) --*

              An array of ``Face`` objects.

              - *(dict) --*

                Describes the face properties such as the bounding box, face ID, image ID of the
                input image, and external image ID that you assigned.

                - **FaceId** *(string) --*

                  Unique identifier that Amazon Rekognition assigns to the face.

                - **BoundingBox** *(dict) --*

                  Bounding box of the face.

                  - **Width** *(float) --*

                    Width of the bounding box as a ratio of the overall image width.

                  - **Height** *(float) --*

                    Height of the bounding box as a ratio of the overall image height.

                  - **Left** *(float) --*

                    Left coordinate of the bounding box as a ratio of overall image width.

                  - **Top** *(float) --*

                    Top coordinate of the bounding box as a ratio of overall image height.

                - **ImageId** *(string) --*

                  Unique identifier that Amazon Rekognition assigns to the input image.

                - **ExternalImageId** *(string) --*

                  Identifier that you assign to all the faces in the input image.

                - **Confidence** *(float) --*

                  Confidence level that the bounding box contains a face (and not a different object
                  such as a tree).

            - **NextToken** *(string) --*

              If the response is truncated, Amazon Rekognition returns this token that you can use
              in the subsequent request to retrieve the next set of faces.

            - **FaceModelVersion** *(string) --*

              Version number of the face detection model associated with the input collection
              (``CollectionId`` ).
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_stream_processors(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListStreamProcessorsResponseTypeDef:
        """
        Gets a list of stream processors that you have created with  CreateStreamProcessor .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/ListStreamProcessors>`_

        **Request Syntax**
        ::

          response = client.list_stream_processors(
              NextToken='string',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken:

          If the previous response was incomplete (because there are more stream processors to
          retrieve), Amazon Rekognition Video returns a pagination token in the response. You can
          use this pagination token to retrieve the next set of stream processors.

        :type MaxResults: integer
        :param MaxResults:

          Maximum number of stream processors you want Amazon Rekognition Video to return in the
          response. The default is 1000.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextToken': 'string',
                'StreamProcessors': [
                    {
                        'Name': 'string',
                        'Status': 'STOPPED'|'STARTING'|'RUNNING'|'FAILED'|'STOPPING'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **NextToken** *(string) --*

              If the response is truncated, Amazon Rekognition Video returns this token that you can
              use in the subsequent request to retrieve the next set of stream processors.

            - **StreamProcessors** *(list) --*

              List of stream processors that you have created.

              - *(dict) --*

                An object that recognizes faces in a streaming video. An Amazon Rekognition stream
                processor is created by a call to  CreateStreamProcessor . The request parameters
                for ``CreateStreamProcessor`` describe the Kinesis video stream source for the
                streaming video, face recognition parameters, and where to stream the analysis
                resullts.

                - **Name** *(string) --*

                  Name of the Amazon Rekognition stream processor.

                - **Status** *(string) --*

                  Current status of the Amazon Rekognition stream processor.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def recognize_celebrities(
        self, Image: ClientRecognizeCelebritiesImageTypeDef
    ) -> ClientRecognizeCelebritiesResponseTypeDef:
        """
        Returns an array of celebrities recognized in the input image. For more information, see
        Recognizing Celebrities in the Amazon Rekognition Developer Guide.

         ``RecognizeCelebrities`` returns the 100 largest faces in the image. It lists recognized
         celebrities in the ``CelebrityFaces`` array and unrecognized faces in the
         ``UnrecognizedFaces`` array. ``RecognizeCelebrities`` doesn't return celebrities whose
         faces aren't among the largest 100 faces in the image.

        For each celebrity recognized, ``RecognizeCelebrities`` returns a ``Celebrity`` object. The
        ``Celebrity`` object contains the celebrity name, ID, URL links to additional information,
        match confidence, and a ``ComparedFace`` object that you can use to locate the celebrity's
        face on the image.

        Amazon Rekognition doesn't retain information about which images a celebrity has been
        recognized in. Your application must store this information and use the ``Celebrity`` ID
        property as a unique identifier for the celebrity. If you don't store the celebrity name or
        additional information URLs returned by ``RecognizeCelebrities`` , you will need the ID to
        identify the celebrity in a call to the  GetCelebrityInfo operation.

        You pass the input image either as base64-encoded image bytes or as a reference to an image
        in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations,
        passing image bytes is not supported. The image must be either a PNG or JPEG formatted file.

        For an example, see Recognizing Celebrities in an Image in the Amazon Rekognition Developer
        Guide.

        This operation requires permissions to perform the ``rekognition:RecognizeCelebrities``
        operation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/RecognizeCelebrities>`_

        **Request Syntax**
        ::

          response = client.recognize_celebrities(
              Image={
                  'Bytes': b'bytes',
                  'S3Object': {
                      'Bucket': 'string',
                      'Name': 'string',
                      'Version': 'string'
                  }
              }
          )
        :type Image: dict
        :param Image: **[REQUIRED]**

          The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call
          Amazon Rekognition operations, passing base64-encoded image bytes is not supported.

          If you are using an AWS SDK to call Amazon Rekognition, you might not need to
          base64-encode image bytes passed using the ``Bytes`` field. For more information, see
          Images in the Amazon Rekognition developer guide.

          - **Bytes** *(bytes) --*

            Blob of image bytes up to 5 MBs.

          - **S3Object** *(dict) --*

            Identifies an S3 object as the image source.

            - **Bucket** *(string) --*

              Name of the S3 bucket.

            - **Name** *(string) --*

              S3 object key name.

            - **Version** *(string) --*

              If the bucket is versioning enabled, you can specify the object version.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CelebrityFaces': [
                    {
                        'Urls': [
                            'string',
                        ],
                        'Name': 'string',
                        'Id': 'string',
                        'Face': {
                            'BoundingBox': {
                                'Width': ...,
                                'Height': ...,
                                'Left': ...,
                                'Top': ...
                            },
                            'Confidence': ...,
                            'Landmarks': [
                                {
                                    'Type':
                                    'eyeLeft'|'eyeRight'|'nose'
                                    |'mouthLeft'|'mouthRight'
                                    |'leftEyeBrowLeft'
                                    |'leftEyeBrowRight'|'leftEyeBrowUp'
                                    |'rightEyeBrowLeft'
                                    |'rightEyeBrowRight'
                                    |'rightEyeBrowUp'|'leftEyeLeft'
                                    |'leftEyeRight'|'leftEyeUp'
                                    |'leftEyeDown'|'rightEyeLeft'
                                    |'rightEyeRight'|'rightEyeUp'
                                    |'rightEyeDown'|'noseLeft'
                                    |'noseRight'|'mouthUp'|'mouthDown'
                                    |'leftPupil'|'rightPupil'
                                    |'upperJawlineLeft'|'midJawlineLeft'
                                    |'chinBottom'|'midJawlineRight'
                                    |'upperJawlineRight',
                                    'X': ...,
                                    'Y': ...
                                },
                            ],
                            'Pose': {
                                'Roll': ...,
                                'Yaw': ...,
                                'Pitch': ...
                            },
                            'Quality': {
                                'Brightness': ...,
                                'Sharpness': ...
                            }
                        },
                        'MatchConfidence': ...
                    },
                ],
                'UnrecognizedFaces': [
                    {
                        'BoundingBox': {
                            'Width': ...,
                            'Height': ...,
                            'Left': ...,
                            'Top': ...
                        },
                        'Confidence': ...,
                        'Landmarks': [
                            {
                                'Type':
                                'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'
                                |'mouthRight'|'leftEyeBrowLeft'
                                |'leftEyeBrowRight'|'leftEyeBrowUp'
                                |'rightEyeBrowLeft'|'rightEyeBrowRight'
                                |'rightEyeBrowUp'|'leftEyeLeft'
                                |'leftEyeRight'|'leftEyeUp'|'leftEyeDown'
                                |'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'
                                |'rightEyeDown'|'noseLeft'|'noseRight'
                                |'mouthUp'|'mouthDown'|'leftPupil'
                                |'rightPupil'|'upperJawlineLeft'
                                |'midJawlineLeft'|'chinBottom'
                                |'midJawlineRight'|'upperJawlineRight',
                                'X': ...,
                                'Y': ...
                            },
                        ],
                        'Pose': {
                            'Roll': ...,
                            'Yaw': ...,
                            'Pitch': ...
                        },
                        'Quality': {
                            'Brightness': ...,
                            'Sharpness': ...
                        }
                    },
                ],
                'OrientationCorrection': 'ROTATE_0'|'ROTATE_90'|'ROTATE_180'|'ROTATE_270'
            }
          **Response Structure**

          - *(dict) --*

            - **CelebrityFaces** *(list) --*

              Details about each celebrity found in the image. Amazon Rekognition can detect a
              maximum of 15 celebrities in an image.

              - *(dict) --*

                Provides information about a celebrity recognized by the  RecognizeCelebrities
                operation.

                - **Urls** *(list) --*

                  An array of URLs pointing to additional information about the celebrity. If there
                  is no additional information about the celebrity, this list is empty.

                  - *(string) --*

                - **Name** *(string) --*

                  The name of the celebrity.

                - **Id** *(string) --*

                  A unique identifier for the celebrity.

                - **Face** *(dict) --*

                  Provides information about the celebrity's face, such as its location on the
                  image.

                  - **BoundingBox** *(dict) --*

                    Bounding box of the face.

                    - **Width** *(float) --*

                      Width of the bounding box as a ratio of the overall image width.

                    - **Height** *(float) --*

                      Height of the bounding box as a ratio of the overall image height.

                    - **Left** *(float) --*

                      Left coordinate of the bounding box as a ratio of overall image width.

                    - **Top** *(float) --*

                      Top coordinate of the bounding box as a ratio of overall image height.

                  - **Confidence** *(float) --*

                    Level of confidence that what the bounding box contains is a face.

                  - **Landmarks** *(list) --*

                    An array of facial landmarks.

                    - *(dict) --*

                      Indicates the location of the landmark on the face.

                      - **Type** *(string) --*

                        Type of landmark.

                      - **X** *(float) --*

                        The x-coordinate from the top left of the landmark expressed as the ratio of
                        the width of the image. For example, if the image is 700 x 200 and the
                        x-coordinate of the landmark is at 350 pixels, this value is 0.5.

                      - **Y** *(float) --*

                        The y-coordinate from the top left of the landmark expressed as the ratio of
                        the height of the image. For example, if the image is 700 x 200 and the
                        y-coordinate of the landmark is at 100 pixels, this value is 0.5.

                  - **Pose** *(dict) --*

                    Indicates the pose of the face as determined by its pitch, roll, and yaw.

                    - **Roll** *(float) --*

                      Value representing the face rotation on the roll axis.

                    - **Yaw** *(float) --*

                      Value representing the face rotation on the yaw axis.

                    - **Pitch** *(float) --*

                      Value representing the face rotation on the pitch axis.

                  - **Quality** *(dict) --*

                    Identifies face image brightness and sharpness.

                    - **Brightness** *(float) --*

                      Value representing brightness of the face. The service returns a value between
                      0 and 100 (inclusive). A higher value indicates a brighter face image.

                    - **Sharpness** *(float) --*

                      Value representing sharpness of the face. The service returns a value between
                      0 and 100 (inclusive). A higher value indicates a sharper face image.

                - **MatchConfidence** *(float) --*

                  The confidence, in percentage, that Amazon Rekognition has that the recognized
                  face is the celebrity.

            - **UnrecognizedFaces** *(list) --*

              Details about each unrecognized face in the image.

              - *(dict) --*

                Provides face metadata for target image faces that are analyzed by ``CompareFaces``
                and ``RecognizeCelebrities`` .

                - **BoundingBox** *(dict) --*

                  Bounding box of the face.

                  - **Width** *(float) --*

                    Width of the bounding box as a ratio of the overall image width.

                  - **Height** *(float) --*

                    Height of the bounding box as a ratio of the overall image height.

                  - **Left** *(float) --*

                    Left coordinate of the bounding box as a ratio of overall image width.

                  - **Top** *(float) --*

                    Top coordinate of the bounding box as a ratio of overall image height.

                - **Confidence** *(float) --*

                  Level of confidence that what the bounding box contains is a face.

                - **Landmarks** *(list) --*

                  An array of facial landmarks.

                  - *(dict) --*

                    Indicates the location of the landmark on the face.

                    - **Type** *(string) --*

                      Type of landmark.

                    - **X** *(float) --*

                      The x-coordinate from the top left of the landmark expressed as the ratio of
                      the width of the image. For example, if the image is 700 x 200 and the
                      x-coordinate of the landmark is at 350 pixels, this value is 0.5.

                    - **Y** *(float) --*

                      The y-coordinate from the top left of the landmark expressed as the ratio of
                      the height of the image. For example, if the image is 700 x 200 and the
                      y-coordinate of the landmark is at 100 pixels, this value is 0.5.

                - **Pose** *(dict) --*

                  Indicates the pose of the face as determined by its pitch, roll, and yaw.

                  - **Roll** *(float) --*

                    Value representing the face rotation on the roll axis.

                  - **Yaw** *(float) --*

                    Value representing the face rotation on the yaw axis.

                  - **Pitch** *(float) --*

                    Value representing the face rotation on the pitch axis.

                - **Quality** *(dict) --*

                  Identifies face image brightness and sharpness.

                  - **Brightness** *(float) --*

                    Value representing brightness of the face. The service returns a value between 0
                    and 100 (inclusive). A higher value indicates a brighter face image.

                  - **Sharpness** *(float) --*

                    Value representing sharpness of the face. The service returns a value between 0
                    and 100 (inclusive). A higher value indicates a sharper face image.

            - **OrientationCorrection** *(string) --*

              The orientation of the input image (counterclockwise direction). If your application
              displays the image, you can use this value to correct the orientation. The bounding
              box coordinates returned in ``CelebrityFaces`` and ``UnrecognizedFaces`` represent
              face locations before the image orientation is corrected.

              .. note::

                If the input image is in .jpeg format, it might contain exchangeable image (Exif)
                metadata that includes the image's orientation. If so, and the Exif metadata for the
                input image populates the orientation field, the value of ``OrientationCorrection``
                is null. The ``CelebrityFaces`` and ``UnrecognizedFaces`` bounding box coordinates
                represent face locations after Exif metadata is used to correct the image
                orientation. Images in .png format don't contain Exif metadata.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def search_faces(
        self, CollectionId: str, FaceId: str, MaxFaces: int = None, FaceMatchThreshold: Any = None
    ) -> ClientSearchFacesResponseTypeDef:
        """
        For a given input face ID, searches for matching faces in the collection the face belongs
        to. You get a face ID when you add a face to the collection using the  IndexFaces operation.
        The operation compares the features of the input face with faces in the specified
        collection.

        .. note::

          You can also search faces without indexing faces by using the ``SearchFacesByImage``
          operation.

        The operation response returns an array of faces that match, ordered by similarity score
        with the highest similarity first. More specifically, it is an array of metadata for each
        face match that is found. Along with the metadata, the response also includes a
        ``confidence`` value for each face match, indicating the confidence that the specific face
        matches the input face.

        For an example, see Searching for a Face Using Its Face ID in the Amazon Rekognition
        Developer Guide.

        This operation requires permissions to perform the ``rekognition:SearchFaces`` action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/SearchFaces>`_

        **Request Syntax**
        ::

          response = client.search_faces(
              CollectionId='string',
              FaceId='string',
              MaxFaces=123,
              FaceMatchThreshold=...
          )
        :type CollectionId: string
        :param CollectionId: **[REQUIRED]**

          ID of the collection the face belongs to.

        :type FaceId: string
        :param FaceId: **[REQUIRED]**

          ID of a face to find matches for in the collection.

        :type MaxFaces: integer
        :param MaxFaces:

          Maximum number of faces to return. The operation returns the maximum number of faces with
          the highest confidence in the match.

        :type FaceMatchThreshold: float
        :param FaceMatchThreshold:

          Optional value specifying the minimum confidence in the face match to return. For example,
          don't return any matches where confidence in matches is less than 70%. The default value
          is 80%.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'SearchedFaceId': 'string',
                'FaceMatches': [
                    {
                        'Similarity': ...,
                        'Face': {
                            'FaceId': 'string',
                            'BoundingBox': {
                                'Width': ...,
                                'Height': ...,
                                'Left': ...,
                                'Top': ...
                            },
                            'ImageId': 'string',
                            'ExternalImageId': 'string',
                            'Confidence': ...
                        }
                    },
                ],
                'FaceModelVersion': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **SearchedFaceId** *(string) --*

              ID of the face that was searched for matches in a collection.

            - **FaceMatches** *(list) --*

              An array of faces that matched the input face, along with the confidence in the match.

              - *(dict) --*

                Provides face metadata. In addition, it also provides the confidence in the match of
                this face with the input face.

                - **Similarity** *(float) --*

                  Confidence in the match of this face with the input face.

                - **Face** *(dict) --*

                  Describes the face properties such as the bounding box, face ID, image ID of the
                  source image, and external image ID that you assigned.

                  - **FaceId** *(string) --*

                    Unique identifier that Amazon Rekognition assigns to the face.

                  - **BoundingBox** *(dict) --*

                    Bounding box of the face.

                    - **Width** *(float) --*

                      Width of the bounding box as a ratio of the overall image width.

                    - **Height** *(float) --*

                      Height of the bounding box as a ratio of the overall image height.

                    - **Left** *(float) --*

                      Left coordinate of the bounding box as a ratio of overall image width.

                    - **Top** *(float) --*

                      Top coordinate of the bounding box as a ratio of overall image height.

                  - **ImageId** *(string) --*

                    Unique identifier that Amazon Rekognition assigns to the input image.

                  - **ExternalImageId** *(string) --*

                    Identifier that you assign to all the faces in the input image.

                  - **Confidence** *(float) --*

                    Confidence level that the bounding box contains a face (and not a different
                    object such as a tree).

            - **FaceModelVersion** *(string) --*

              Version number of the face detection model associated with the input collection
              (``CollectionId`` ).
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def search_faces_by_image(
        self,
        CollectionId: str,
        Image: ClientSearchFacesByImageImageTypeDef,
        MaxFaces: int = None,
        FaceMatchThreshold: Any = None,
        QualityFilter: Literal["NONE", "AUTO", "LOW", "MEDIUM", "HIGH"] = None,
    ) -> ClientSearchFacesByImageResponseTypeDef:
        """
        For a given input image, first detects the largest face in the image, and then searches the
        specified collection for matching faces. The operation compares the features of the input
        face with faces in the specified collection.

        .. note::

          To search for all faces in an input image, you might first call the  IndexFaces operation,
          and then use the face IDs returned in subsequent calls to the  SearchFaces operation.

          You can also call the ``DetectFaces`` operation and use the bounding boxes in the response
          to make face crops, which then you can pass in to the ``SearchFacesByImage`` operation.

        You pass the input image either as base64-encoded image bytes or as a reference to an image
        in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations,
        passing image bytes is not supported. The image must be either a PNG or JPEG formatted file.

        The response returns an array of faces that match, ordered by similarity score with the
        highest similarity first. More specifically, it is an array of metadata for each face match
        found. Along with the metadata, the response also includes a ``similarity`` indicating how
        similar the face is to the input face. In the response, the operation also returns the
        bounding box (and a confidence level that the bounding box contains a face) of the face that
        Amazon Rekognition used for the input image.

        For an example, Searching for a Face Using an Image in the Amazon Rekognition Developer
        Guide.

        The ``QualityFilter`` input parameter allows you to filter out detected faces that don’t
        meet a required quality bar. The quality bar is based on a variety of common use cases. Use
        ``QualityFilter`` to set the quality bar for filtering by specifying ``LOW`` , ``MEDIUM`` ,
        or ``HIGH`` . If you do not want to filter detected faces, specify ``NONE`` . The default
        value is ``NONE`` .

        .. note::

          To use quality filtering, you need a collection associated with version 3 of the face
          model or higher. To get the version of the face model associated with a collection, call
          DescribeCollection .

        This operation requires permissions to perform the ``rekognition:SearchFacesByImage``
        action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/SearchFacesByImage>`_

        **Request Syntax**
        ::

          response = client.search_faces_by_image(
              CollectionId='string',
              Image={
                  'Bytes': b'bytes',
                  'S3Object': {
                      'Bucket': 'string',
                      'Name': 'string',
                      'Version': 'string'
                  }
              },
              MaxFaces=123,
              FaceMatchThreshold=...,
              QualityFilter='NONE'|'AUTO'|'LOW'|'MEDIUM'|'HIGH'
          )
        :type CollectionId: string
        :param CollectionId: **[REQUIRED]**

          ID of the collection to search.

        :type Image: dict
        :param Image: **[REQUIRED]**

          The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call
          Amazon Rekognition operations, passing base64-encoded image bytes is not supported.

          If you are using an AWS SDK to call Amazon Rekognition, you might not need to
          base64-encode image bytes passed using the ``Bytes`` field. For more information, see
          Images in the Amazon Rekognition developer guide.

          - **Bytes** *(bytes) --*

            Blob of image bytes up to 5 MBs.

          - **S3Object** *(dict) --*

            Identifies an S3 object as the image source.

            - **Bucket** *(string) --*

              Name of the S3 bucket.

            - **Name** *(string) --*

              S3 object key name.

            - **Version** *(string) --*

              If the bucket is versioning enabled, you can specify the object version.

        :type MaxFaces: integer
        :param MaxFaces:

          Maximum number of faces to return. The operation returns the maximum number of faces with
          the highest confidence in the match.

        :type FaceMatchThreshold: float
        :param FaceMatchThreshold:

          (Optional) Specifies the minimum confidence in the face match to return. For example,
          don't return any matches where confidence in matches is less than 70%. The default value
          is 80%.

        :type QualityFilter: string
        :param QualityFilter:

          A filter that specifies a quality bar for how much filtering is done to identify faces.
          Filtered faces aren't searched for in the collection. If you specify ``AUTO`` , Amazon
          Rekognition chooses the quality bar. If you specify ``LOW`` , ``MEDIUM`` , or ``HIGH`` ,
          filtering removes all faces that don’t meet the chosen quality bar. The quality bar is
          based on a variety of common use cases. Low-quality detections can occur for a number of
          reasons. Some examples are an object that's misidentified as a face, a face that's too
          blurry, or a face with a pose that's too extreme to use. If you specify ``NONE`` , no
          filtering is performed. The default value is ``NONE`` .

          To use quality filtering, the collection you are using must be associated with version 3
          of the face model or higher.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'SearchedFaceBoundingBox': {
                    'Width': ...,
                    'Height': ...,
                    'Left': ...,
                    'Top': ...
                },
                'SearchedFaceConfidence': ...,
                'FaceMatches': [
                    {
                        'Similarity': ...,
                        'Face': {
                            'FaceId': 'string',
                            'BoundingBox': {
                                'Width': ...,
                                'Height': ...,
                                'Left': ...,
                                'Top': ...
                            },
                            'ImageId': 'string',
                            'ExternalImageId': 'string',
                            'Confidence': ...
                        }
                    },
                ],
                'FaceModelVersion': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **SearchedFaceBoundingBox** *(dict) --*

              The bounding box around the face in the input image that Amazon Rekognition used for
              the search.

              - **Width** *(float) --*

                Width of the bounding box as a ratio of the overall image width.

              - **Height** *(float) --*

                Height of the bounding box as a ratio of the overall image height.

              - **Left** *(float) --*

                Left coordinate of the bounding box as a ratio of overall image width.

              - **Top** *(float) --*

                Top coordinate of the bounding box as a ratio of overall image height.

            - **SearchedFaceConfidence** *(float) --*

              The level of confidence that the ``searchedFaceBoundingBox`` , contains a face.

            - **FaceMatches** *(list) --*

              An array of faces that match the input face, along with the confidence in the match.

              - *(dict) --*

                Provides face metadata. In addition, it also provides the confidence in the match of
                this face with the input face.

                - **Similarity** *(float) --*

                  Confidence in the match of this face with the input face.

                - **Face** *(dict) --*

                  Describes the face properties such as the bounding box, face ID, image ID of the
                  source image, and external image ID that you assigned.

                  - **FaceId** *(string) --*

                    Unique identifier that Amazon Rekognition assigns to the face.

                  - **BoundingBox** *(dict) --*

                    Bounding box of the face.

                    - **Width** *(float) --*

                      Width of the bounding box as a ratio of the overall image width.

                    - **Height** *(float) --*

                      Height of the bounding box as a ratio of the overall image height.

                    - **Left** *(float) --*

                      Left coordinate of the bounding box as a ratio of overall image width.

                    - **Top** *(float) --*

                      Top coordinate of the bounding box as a ratio of overall image height.

                  - **ImageId** *(string) --*

                    Unique identifier that Amazon Rekognition assigns to the input image.

                  - **ExternalImageId** *(string) --*

                    Identifier that you assign to all the faces in the input image.

                  - **Confidence** *(float) --*

                    Confidence level that the bounding box contains a face (and not a different
                    object such as a tree).

            - **FaceModelVersion** *(string) --*

              Version number of the face detection model associated with the input collection
              (``CollectionId`` ).
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_celebrity_recognition(
        self,
        Video: ClientStartCelebrityRecognitionVideoTypeDef,
        ClientRequestToken: str = None,
        NotificationChannel: ClientStartCelebrityRecognitionNotificationChannelTypeDef = None,
        JobTag: str = None,
    ) -> ClientStartCelebrityRecognitionResponseTypeDef:
        """
        Starts asynchronous recognition of celebrities in a stored video.

        Amazon Rekognition Video can detect celebrities in a video must be stored in an Amazon S3
        bucket. Use  Video to specify the bucket name and the filename of the video.
        ``StartCelebrityRecognition`` returns a job identifier (``JobId`` ) which you use to get the
        results of the analysis. When celebrity recognition analysis is finished, Amazon Rekognition
        Video publishes a completion status to the Amazon Simple Notification Service topic that you
        specify in ``NotificationChannel`` . To get the results of the celebrity recognition
        analysis, first check that the status value published to the Amazon SNS topic is
        ``SUCCEEDED`` . If so, call  GetCelebrityRecognition and pass the job identifier (``JobId``
        ) from the initial call to ``StartCelebrityRecognition`` .

        For more information, see Recognizing Celebrities in the Amazon Rekognition Developer Guide.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/StartCelebrityRecognition>`_

        **Request Syntax**
        ::

          response = client.start_celebrity_recognition(
              Video={
                  'S3Object': {
                      'Bucket': 'string',
                      'Name': 'string',
                      'Version': 'string'
                  }
              },
              ClientRequestToken='string',
              NotificationChannel={
                  'SNSTopicArn': 'string',
                  'RoleArn': 'string'
              },
              JobTag='string'
          )
        :type Video: dict
        :param Video: **[REQUIRED]**

          The video in which you want to recognize celebrities. The video must be stored in an
          Amazon S3 bucket.

          - **S3Object** *(dict) --*

            The Amazon S3 bucket name and file name for the video.

            - **Bucket** *(string) --*

              Name of the S3 bucket.

            - **Name** *(string) --*

              S3 object key name.

            - **Version** *(string) --*

              If the bucket is versioning enabled, you can specify the object version.

        :type ClientRequestToken: string
        :param ClientRequestToken:

          Idempotent token used to identify the start request. If you use the same token with
          multiple ``StartCelebrityRecognition`` requests, the same ``JobId`` is returned. Use
          ``ClientRequestToken`` to prevent the same job from being accidently started more than
          once.

        :type NotificationChannel: dict
        :param NotificationChannel:

          The Amazon SNS topic ARN that you want Amazon Rekognition Video to publish the completion
          status of the celebrity recognition analysis to.

          - **SNSTopicArn** *(string) --* **[REQUIRED]**

            The Amazon SNS topic to which Amazon Rekognition to posts the completion status.

          - **RoleArn** *(string) --* **[REQUIRED]**

            The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the
            Amazon SNS topic.

        :type JobTag: string
        :param JobTag:

          An identifier you specify that's returned in the completion notification that's published
          to your Amazon Simple Notification Service topic. For example, you can use ``JobTag`` to
          group related jobs and identify them in the completion notification.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **JobId** *(string) --*

              The identifier for the celebrity recognition analysis job. Use ``JobId`` to identify
              the job in a subsequent call to ``GetCelebrityRecognition`` .
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_content_moderation(
        self,
        Video: ClientStartContentModerationVideoTypeDef,
        MinConfidence: Any = None,
        ClientRequestToken: str = None,
        NotificationChannel: ClientStartContentModerationNotificationChannelTypeDef = None,
        JobTag: str = None,
    ) -> ClientStartContentModerationResponseTypeDef:
        """
        Starts asynchronous detection of unsafe content in a stored video.

        Amazon Rekognition Video can moderate content in a video stored in an Amazon S3 bucket. Use
        Video to specify the bucket name and the filename of the video. ``StartContentModeration``
        returns a job identifier (``JobId`` ) which you use to get the results of the analysis. When
        unsafe content analysis is finished, Amazon Rekognition Video publishes a completion status
        to the Amazon Simple Notification Service topic that you specify in ``NotificationChannel``
        .

        To get the results of the unsafe content analysis, first check that the status value
        published to the Amazon SNS topic is ``SUCCEEDED`` . If so, call  GetContentModeration and
        pass the job identifier (``JobId`` ) from the initial call to ``StartContentModeration`` .

        For more information, see Detecting Unsafe Content in the Amazon Rekognition Developer
        Guide.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/StartContentModeration>`_

        **Request Syntax**
        ::

          response = client.start_content_moderation(
              Video={
                  'S3Object': {
                      'Bucket': 'string',
                      'Name': 'string',
                      'Version': 'string'
                  }
              },
              MinConfidence=...,
              ClientRequestToken='string',
              NotificationChannel={
                  'SNSTopicArn': 'string',
                  'RoleArn': 'string'
              },
              JobTag='string'
          )
        :type Video: dict
        :param Video: **[REQUIRED]**

          The video in which you want to detect unsafe content. The video must be stored in an
          Amazon S3 bucket.

          - **S3Object** *(dict) --*

            The Amazon S3 bucket name and file name for the video.

            - **Bucket** *(string) --*

              Name of the S3 bucket.

            - **Name** *(string) --*

              S3 object key name.

            - **Version** *(string) --*

              If the bucket is versioning enabled, you can specify the object version.

        :type MinConfidence: float
        :param MinConfidence:

          Specifies the minimum confidence that Amazon Rekognition must have in order to return a
          moderated content label. Confidence represents how certain Amazon Rekognition is that the
          moderated content is correctly identified. 0 is the lowest confidence. 100 is the highest
          confidence. Amazon Rekognition doesn't return any moderated content labels with a
          confidence level lower than this specified value. If you don't specify ``MinConfidence`` ,
          ``GetContentModeration`` returns labels with confidence values greater than or equal to 50
          percent.

        :type ClientRequestToken: string
        :param ClientRequestToken:

          Idempotent token used to identify the start request. If you use the same token with
          multiple ``StartContentModeration`` requests, the same ``JobId`` is returned. Use
          ``ClientRequestToken`` to prevent the same job from being accidently started more than
          once.

        :type NotificationChannel: dict
        :param NotificationChannel:

          The Amazon SNS topic ARN that you want Amazon Rekognition Video to publish the completion
          status of the unsafe content analysis to.

          - **SNSTopicArn** *(string) --* **[REQUIRED]**

            The Amazon SNS topic to which Amazon Rekognition to posts the completion status.

          - **RoleArn** *(string) --* **[REQUIRED]**

            The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the
            Amazon SNS topic.

        :type JobTag: string
        :param JobTag:

          An identifier you specify that's returned in the completion notification that's published
          to your Amazon Simple Notification Service topic. For example, you can use ``JobTag`` to
          group related jobs and identify them in the completion notification.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **JobId** *(string) --*

              The identifier for the unsafe content analysis job. Use ``JobId`` to identify the job
              in a subsequent call to ``GetContentModeration`` .
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_face_detection(
        self,
        Video: ClientStartFaceDetectionVideoTypeDef,
        ClientRequestToken: str = None,
        NotificationChannel: ClientStartFaceDetectionNotificationChannelTypeDef = None,
        FaceAttributes: Literal["DEFAULT", "ALL"] = None,
        JobTag: str = None,
    ) -> ClientStartFaceDetectionResponseTypeDef:
        """
        Starts asynchronous detection of faces in a stored video.

        Amazon Rekognition Video can detect faces in a video stored in an Amazon S3 bucket. Use
        Video to specify the bucket name and the filename of the video. ``StartFaceDetection``
        returns a job identifier (``JobId`` ) that you use to get the results of the operation. When
        face detection is finished, Amazon Rekognition Video publishes a completion status to the
        Amazon Simple Notification Service topic that you specify in ``NotificationChannel`` . To
        get the results of the face detection operation, first check that the status value published
        to the Amazon SNS topic is ``SUCCEEDED`` . If so, call  GetFaceDetection and pass the job
        identifier (``JobId`` ) from the initial call to ``StartFaceDetection`` .

        For more information, see Detecting Faces in a Stored Video in the Amazon Rekognition
        Developer Guide.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/StartFaceDetection>`_

        **Request Syntax**
        ::

          response = client.start_face_detection(
              Video={
                  'S3Object': {
                      'Bucket': 'string',
                      'Name': 'string',
                      'Version': 'string'
                  }
              },
              ClientRequestToken='string',
              NotificationChannel={
                  'SNSTopicArn': 'string',
                  'RoleArn': 'string'
              },
              FaceAttributes='DEFAULT'|'ALL',
              JobTag='string'
          )
        :type Video: dict
        :param Video: **[REQUIRED]**

          The video in which you want to detect faces. The video must be stored in an Amazon S3
          bucket.

          - **S3Object** *(dict) --*

            The Amazon S3 bucket name and file name for the video.

            - **Bucket** *(string) --*

              Name of the S3 bucket.

            - **Name** *(string) --*

              S3 object key name.

            - **Version** *(string) --*

              If the bucket is versioning enabled, you can specify the object version.

        :type ClientRequestToken: string
        :param ClientRequestToken:

          Idempotent token used to identify the start request. If you use the same token with
          multiple ``StartFaceDetection`` requests, the same ``JobId`` is returned. Use
          ``ClientRequestToken`` to prevent the same job from being accidently started more than
          once.

        :type NotificationChannel: dict
        :param NotificationChannel:

          The ARN of the Amazon SNS topic to which you want Amazon Rekognition Video to publish the
          completion status of the face detection operation.

          - **SNSTopicArn** *(string) --* **[REQUIRED]**

            The Amazon SNS topic to which Amazon Rekognition to posts the completion status.

          - **RoleArn** *(string) --* **[REQUIRED]**

            The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the
            Amazon SNS topic.

        :type FaceAttributes: string
        :param FaceAttributes:

          The face attributes you want returned.

           ``DEFAULT`` - The following subset of facial attributes are returned: BoundingBox,
           Confidence, Pose, Quality and Landmarks.

           ``ALL`` - All facial attributes are returned.

        :type JobTag: string
        :param JobTag:

          An identifier you specify that's returned in the completion notification that's published
          to your Amazon Simple Notification Service topic. For example, you can use ``JobTag`` to
          group related jobs and identify them in the completion notification.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **JobId** *(string) --*

              The identifier for the face detection job. Use ``JobId`` to identify the job in a
              subsequent call to ``GetFaceDetection`` .
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_face_search(
        self,
        Video: ClientStartFaceSearchVideoTypeDef,
        CollectionId: str,
        ClientRequestToken: str = None,
        FaceMatchThreshold: Any = None,
        NotificationChannel: ClientStartFaceSearchNotificationChannelTypeDef = None,
        JobTag: str = None,
    ) -> ClientStartFaceSearchResponseTypeDef:
        """
        Starts the asynchronous search for faces in a collection that match the faces of persons
        detected in a stored video.

        The video must be stored in an Amazon S3 bucket. Use  Video to specify the bucket name and
        the filename of the video. ``StartFaceSearch`` returns a job identifier (``JobId`` ) which
        you use to get the search results once the search has completed. When searching is finished,
        Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification
        Service topic that you specify in ``NotificationChannel`` . To get the search results, first
        check that the status value published to the Amazon SNS topic is ``SUCCEEDED`` . If so, call
        GetFaceSearch and pass the job identifier (``JobId`` ) from the initial call to
        ``StartFaceSearch`` . For more information, see  procedure-person-search-videos .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/StartFaceSearch>`_

        **Request Syntax**
        ::

          response = client.start_face_search(
              Video={
                  'S3Object': {
                      'Bucket': 'string',
                      'Name': 'string',
                      'Version': 'string'
                  }
              },
              ClientRequestToken='string',
              FaceMatchThreshold=...,
              CollectionId='string',
              NotificationChannel={
                  'SNSTopicArn': 'string',
                  'RoleArn': 'string'
              },
              JobTag='string'
          )
        :type Video: dict
        :param Video: **[REQUIRED]**

          The video you want to search. The video must be stored in an Amazon S3 bucket.

          - **S3Object** *(dict) --*

            The Amazon S3 bucket name and file name for the video.

            - **Bucket** *(string) --*

              Name of the S3 bucket.

            - **Name** *(string) --*

              S3 object key name.

            - **Version** *(string) --*

              If the bucket is versioning enabled, you can specify the object version.

        :type ClientRequestToken: string
        :param ClientRequestToken:

          Idempotent token used to identify the start request. If you use the same token with
          multiple ``StartFaceSearch`` requests, the same ``JobId`` is returned. Use
          ``ClientRequestToken`` to prevent the same job from being accidently started more than
          once.

        :type FaceMatchThreshold: float
        :param FaceMatchThreshold:

          The minimum confidence in the person match to return. For example, don't return any
          matches where confidence in matches is less than 70%. The default value is 80%.

        :type CollectionId: string
        :param CollectionId: **[REQUIRED]**

          ID of the collection that contains the faces you want to search for.

        :type NotificationChannel: dict
        :param NotificationChannel:

          The ARN of the Amazon SNS topic to which you want Amazon Rekognition Video to publish the
          completion status of the search.

          - **SNSTopicArn** *(string) --* **[REQUIRED]**

            The Amazon SNS topic to which Amazon Rekognition to posts the completion status.

          - **RoleArn** *(string) --* **[REQUIRED]**

            The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the
            Amazon SNS topic.

        :type JobTag: string
        :param JobTag:

          An identifier you specify that's returned in the completion notification that's published
          to your Amazon Simple Notification Service topic. For example, you can use ``JobTag`` to
          group related jobs and identify them in the completion notification.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **JobId** *(string) --*

              The identifier for the search job. Use ``JobId`` to identify the job in a subsequent
              call to ``GetFaceSearch`` .
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_label_detection(
        self,
        Video: ClientStartLabelDetectionVideoTypeDef,
        ClientRequestToken: str = None,
        MinConfidence: Any = None,
        NotificationChannel: ClientStartLabelDetectionNotificationChannelTypeDef = None,
        JobTag: str = None,
    ) -> ClientStartLabelDetectionResponseTypeDef:
        """
        Starts asynchronous detection of labels in a stored video.

        Amazon Rekognition Video can detect labels in a video. Labels are instances of real-world
        entities. This includes objects like flower, tree, and table; events like wedding,
        graduation, and birthday party; concepts like landscape, evening, and nature; and activities
        like a person getting out of a car or a person skiing.

        The video must be stored in an Amazon S3 bucket. Use  Video to specify the bucket name and
        the filename of the video. ``StartLabelDetection`` returns a job identifier (``JobId`` )
        which you use to get the results of the operation. When label detection is finished, Amazon
        Rekognition Video publishes a completion status to the Amazon Simple Notification Service
        topic that you specify in ``NotificationChannel`` .

        To get the results of the label detection operation, first check that the status value
        published to the Amazon SNS topic is ``SUCCEEDED`` . If so, call  GetLabelDetection and pass
        the job identifier (``JobId`` ) from the initial call to ``StartLabelDetection`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/StartLabelDetection>`_

        **Request Syntax**
        ::

          response = client.start_label_detection(
              Video={
                  'S3Object': {
                      'Bucket': 'string',
                      'Name': 'string',
                      'Version': 'string'
                  }
              },
              ClientRequestToken='string',
              MinConfidence=...,
              NotificationChannel={
                  'SNSTopicArn': 'string',
                  'RoleArn': 'string'
              },
              JobTag='string'
          )
        :type Video: dict
        :param Video: **[REQUIRED]**

          The video in which you want to detect labels. The video must be stored in an Amazon S3
          bucket.

          - **S3Object** *(dict) --*

            The Amazon S3 bucket name and file name for the video.

            - **Bucket** *(string) --*

              Name of the S3 bucket.

            - **Name** *(string) --*

              S3 object key name.

            - **Version** *(string) --*

              If the bucket is versioning enabled, you can specify the object version.

        :type ClientRequestToken: string
        :param ClientRequestToken:

          Idempotent token used to identify the start request. If you use the same token with
          multiple ``StartLabelDetection`` requests, the same ``JobId`` is returned. Use
          ``ClientRequestToken`` to prevent the same job from being accidently started more than
          once.

        :type MinConfidence: float
        :param MinConfidence:

          Specifies the minimum confidence that Amazon Rekognition Video must have in order to
          return a detected label. Confidence represents how certain Amazon Rekognition is that a
          label is correctly identified.0 is the lowest confidence. 100 is the highest confidence.
          Amazon Rekognition Video doesn't return any labels with a confidence level lower than this
          specified value.

          If you don't specify ``MinConfidence`` , the operation returns labels with confidence
          values greater than or equal to 50 percent.

        :type NotificationChannel: dict
        :param NotificationChannel:

          The Amazon SNS topic ARN you want Amazon Rekognition Video to publish the completion
          status of the label detection operation to.

          - **SNSTopicArn** *(string) --* **[REQUIRED]**

            The Amazon SNS topic to which Amazon Rekognition to posts the completion status.

          - **RoleArn** *(string) --* **[REQUIRED]**

            The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the
            Amazon SNS topic.

        :type JobTag: string
        :param JobTag:

          An identifier you specify that's returned in the completion notification that's published
          to your Amazon Simple Notification Service topic. For example, you can use ``JobTag`` to
          group related jobs and identify them in the completion notification.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **JobId** *(string) --*

              The identifier for the label detection job. Use ``JobId`` to identify the job in a
              subsequent call to ``GetLabelDetection`` .
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_person_tracking(
        self,
        Video: ClientStartPersonTrackingVideoTypeDef,
        ClientRequestToken: str = None,
        NotificationChannel: ClientStartPersonTrackingNotificationChannelTypeDef = None,
        JobTag: str = None,
    ) -> ClientStartPersonTrackingResponseTypeDef:
        """
        Starts the asynchronous tracking of a person's path in a stored video.

        Amazon Rekognition Video can track the path of people in a video stored in an Amazon S3
        bucket. Use  Video to specify the bucket name and the filename of the video.
        ``StartPersonTracking`` returns a job identifier (``JobId`` ) which you use to get the
        results of the operation. When label detection is finished, Amazon Rekognition publishes a
        completion status to the Amazon Simple Notification Service topic that you specify in
        ``NotificationChannel`` .

        To get the results of the person detection operation, first check that the status value
        published to the Amazon SNS topic is ``SUCCEEDED`` . If so, call  GetPersonTracking and pass
        the job identifier (``JobId`` ) from the initial call to ``StartPersonTracking`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/StartPersonTracking>`_

        **Request Syntax**
        ::

          response = client.start_person_tracking(
              Video={
                  'S3Object': {
                      'Bucket': 'string',
                      'Name': 'string',
                      'Version': 'string'
                  }
              },
              ClientRequestToken='string',
              NotificationChannel={
                  'SNSTopicArn': 'string',
                  'RoleArn': 'string'
              },
              JobTag='string'
          )
        :type Video: dict
        :param Video: **[REQUIRED]**

          The video in which you want to detect people. The video must be stored in an Amazon S3
          bucket.

          - **S3Object** *(dict) --*

            The Amazon S3 bucket name and file name for the video.

            - **Bucket** *(string) --*

              Name of the S3 bucket.

            - **Name** *(string) --*

              S3 object key name.

            - **Version** *(string) --*

              If the bucket is versioning enabled, you can specify the object version.

        :type ClientRequestToken: string
        :param ClientRequestToken:

          Idempotent token used to identify the start request. If you use the same token with
          multiple ``StartPersonTracking`` requests, the same ``JobId`` is returned. Use
          ``ClientRequestToken`` to prevent the same job from being accidently started more than
          once.

        :type NotificationChannel: dict
        :param NotificationChannel:

          The Amazon SNS topic ARN you want Amazon Rekognition Video to publish the completion
          status of the people detection operation to.

          - **SNSTopicArn** *(string) --* **[REQUIRED]**

            The Amazon SNS topic to which Amazon Rekognition to posts the completion status.

          - **RoleArn** *(string) --* **[REQUIRED]**

            The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the
            Amazon SNS topic.

        :type JobTag: string
        :param JobTag:

          An identifier you specify that's returned in the completion notification that's published
          to your Amazon Simple Notification Service topic. For example, you can use ``JobTag`` to
          group related jobs and identify them in the completion notification.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **JobId** *(string) --*

              The identifier for the person detection job. Use ``JobId`` to identify the job in a
              subsequent call to ``GetPersonTracking`` .
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_project_version(
        self, ProjectVersionArn: str, MinInferenceUnits: int
    ) -> ClientStartProjectVersionResponseTypeDef:
        """
        Starts the running of the version of a model. Starting a model takes a while to complete. To
        check the current state of the model, use  DescribeProjectVersions .

        Once the model is running, you can detect custom labels in new images by calling
        DetectCustomLabels .

        .. note::

          You are charged for the amount of time that the model is running. To stop a running model,
          call  StopProjectVersion .

        This operation requires permissions to perform the ``rekognition:StartProjectVersion``
        action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/StartProjectVersion>`_

        **Request Syntax**
        ::

          response = client.start_project_version(
              ProjectVersionArn='string',
              MinInferenceUnits=123
          )
        :type ProjectVersionArn: string
        :param ProjectVersionArn: **[REQUIRED]**

          The Amazon Resource Name(ARN) of the model version that you want to start.

        :type MinInferenceUnits: integer
        :param MinInferenceUnits: **[REQUIRED]**

          The minimum number of inference units to use. A single inference unit represents 1 hour of
          processing and can support up to 5 Transaction Pers Second (TPS). Use a higher number to
          increase the TPS throughput of your model. You are charged for the number of inference
          units that you use.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Status':
                'TRAINING_IN_PROGRESS'|'TRAINING_COMPLETED'|'TRAINING_FAILED'|'STARTING'
                |'RUNNING'|'FAILED'|'STOPPING'|'STOPPED'|'DELETING'
            }
          **Response Structure**

          - *(dict) --*

            - **Status** *(string) --*

              The current running status of the model.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_stream_processor(self, Name: str) -> Dict[str, Any]:
        """
        Starts processing a stream processor. You create a stream processor by calling
        CreateStreamProcessor . To tell ``StartStreamProcessor`` which stream processor to start,
        use the value of the ``Name`` field specified in the call to ``CreateStreamProcessor`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/StartStreamProcessor>`_

        **Request Syntax**
        ::

          response = client.start_stream_processor(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the stream processor to start processing.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_project_version(
        self, ProjectVersionArn: str
    ) -> ClientStopProjectVersionResponseTypeDef:
        """
        Stops a running model. The operation might take a while to complete. To check the current
        status, call  DescribeProjectVersions .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/StopProjectVersion>`_

        **Request Syntax**
        ::

          response = client.stop_project_version(
              ProjectVersionArn='string'
          )
        :type ProjectVersionArn: string
        :param ProjectVersionArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the model version that you want to delete.

          This operation requires permissions to perform the ``rekognition:StopProjectVersion``
          action.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Status':
                'TRAINING_IN_PROGRESS'|'TRAINING_COMPLETED'|'TRAINING_FAILED'|'STARTING'
                |'RUNNING'|'FAILED'|'STOPPING'|'STOPPED'|'DELETING'
            }
          **Response Structure**

          - *(dict) --*

            - **Status** *(string) --*

              The current status of the stop operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_stream_processor(self, Name: str) -> Dict[str, Any]:
        """
        Stops a running stream processor that was created by  CreateStreamProcessor .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/StopStreamProcessor>`_

        **Request Syntax**
        ::

          response = client.stop_stream_processor(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of a stream processor created by  CreateStreamProcessor .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_project_versions"]
    ) -> paginator_scope.DescribeProjectVersionsPaginator:
        """
        Get Paginator for `describe_project_versions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_projects"]
    ) -> paginator_scope.DescribeProjectsPaginator:
        """
        Get Paginator for `describe_projects` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_collections"]
    ) -> paginator_scope.ListCollectionsPaginator:
        """
        Get Paginator for `list_collections` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_faces"]
    ) -> paginator_scope.ListFacesPaginator:
        """
        Get Paginator for `list_faces` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_stream_processors"]
    ) -> paginator_scope.ListStreamProcessorsPaginator:
        """
        Get Paginator for `list_stream_processors` operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        """
        Create a paginator for an operation.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :raise OperationNotPageableError: Raised if the operation is not
            pageable.  You can use the ``client.can_paginate`` method to
            check if an operation is pageable.

        :rtype: L{botocore.paginate.Paginator}
        :return: A paginator object.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["project_version_running"]
    ) -> waiter_scope.ProjectVersionRunningWaiter:
        """
        Get Waiter `project_version_running`.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["project_version_training_completed"]
    ) -> waiter_scope.ProjectVersionTrainingCompletedWaiter:
        """
        Get Waiter `project_version_training_completed`.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(self, waiter_name: str) -> Boto3Waiter:
        """
        Returns an object that can wait for some condition.

        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.

        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """


class Exceptions:
    AccessDeniedException: Boto3ClientError
    ClientError: Boto3ClientError
    HumanLoopQuotaExceededException: Boto3ClientError
    IdempotentParameterMismatchException: Boto3ClientError
    ImageTooLargeException: Boto3ClientError
    InternalServerError: Boto3ClientError
    InvalidImageFormatException: Boto3ClientError
    InvalidPaginationTokenException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidS3ObjectException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ProvisionedThroughputExceededException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourceNotReadyException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    VideoTooLargeException: Boto3ClientError
