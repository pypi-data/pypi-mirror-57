"Main interface for transcribe service Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from mypy_boto3.type_defs import Literal

# pylint: disable=import-self
import mypy_boto3_transcribe.client as client_scope
from mypy_boto3_transcribe.type_defs import (
    ClientCreateVocabularyResponseTypeDef,
    ClientGetTranscriptionJobResponseTypeDef,
    ClientGetVocabularyResponseTypeDef,
    ClientListTranscriptionJobsResponseTypeDef,
    ClientListVocabulariesResponseTypeDef,
    ClientStartTranscriptionJobMediaTypeDef,
    ClientStartTranscriptionJobResponseTypeDef,
    ClientStartTranscriptionJobSettingsTypeDef,
    ClientUpdateVocabularyResponseTypeDef,
)


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
    def create_vocabulary(
        self,
        VocabularyName: str,
        LanguageCode: Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        Phrases: List[str] = None,
        VocabularyFileUri: str = None,
    ) -> ClientCreateVocabularyResponseTypeDef:
        """
        Creates a new custom vocabulary that you can use to change the way Amazon Transcribe handles
        transcription of an audio file.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/CreateVocabulary>`_

        **Request Syntax**
        ::

          response = client.create_vocabulary(
              VocabularyName='string',
              LanguageCode=
                  'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'
                  |'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'
                  |'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'
                  |'ar-AE',
              Phrases=[
                  'string',
              ],
              VocabularyFileUri='string'
          )
        :type VocabularyName: string
        :param VocabularyName: **[REQUIRED]**

          The name of the vocabulary. The name must be unique within an AWS account. The name is
          case-sensitive.

        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]**

          The language code of the vocabulary entries.

        :type Phrases: list
        :param Phrases:

          An array of strings that contains the vocabulary entries.

          - *(string) --*

        :type VocabularyFileUri: string
        :param VocabularyFileUri:

          The S3 location of the text file that contains the definition of the custom vocabulary.
          The URI must be in the same region as the API endpoint that you are calling. The general
          form is

           ``https://s3.<aws-region>.amazonaws.com/<bucket-name>/<keyprefix>/<objectkey>``

          For example:

           ``https://s3.us-east-1.amazonaws.com/examplebucket/vocab.txt``

          For more information about S3 object names, see `Object Keys
          <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#object-keys>`__ in the
          *Amazon S3 Developer Guide* .

          For more information about custom vocabularies, see `Custom Vocabularies
          <http://docs.aws.amazon.com/transcribe/latest/dg/how-it-works.html#how-vocabulary>`__ .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'VocabularyName': 'string',
                'LanguageCode':
                'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'
                |'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'
                |'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'
                |'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
                'VocabularyState': 'PENDING'|'READY'|'FAILED',
                'LastModifiedTime': datetime(2015, 1, 1),
                'FailureReason': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **VocabularyName** *(string) --*

              The name of the vocabulary.

            - **LanguageCode** *(string) --*

              The language code of the vocabulary entries.

            - **VocabularyState** *(string) --*

              The processing state of the vocabulary. When the ``VocabularyState`` field contains
              ``READY`` the vocabulary is ready to be used in a ``StartTranscriptionJob`` request.

            - **LastModifiedTime** *(datetime) --*

              The date and time that the vocabulary was created.

            - **FailureReason** *(string) --*

              If the ``VocabularyState`` field is ``FAILED`` , this field contains information about
              why the job failed.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_transcription_job(self, TranscriptionJobName: str) -> None:
        """
        Deletes a previously submitted transcription job along with any other generated results such
        as the transcription, models, and so on.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/DeleteTranscriptionJob>`_

        **Request Syntax**
        ::

          response = client.delete_transcription_job(
              TranscriptionJobName='string'
          )
        :type TranscriptionJobName: string
        :param TranscriptionJobName: **[REQUIRED]**

          The name of the transcription job to be deleted.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_vocabulary(self, VocabularyName: str) -> None:
        """
        Deletes a vocabulary from Amazon Transcribe.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/DeleteVocabulary>`_

        **Request Syntax**
        ::

          response = client.delete_vocabulary(
              VocabularyName='string'
          )
        :type VocabularyName: string
        :param VocabularyName: **[REQUIRED]**

          The name of the vocabulary to delete.

        :returns: None
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
    def get_transcription_job(
        self, TranscriptionJobName: str
    ) -> ClientGetTranscriptionJobResponseTypeDef:
        """
        Returns information about a transcription job. To see the status of the job, check the
        ``TranscriptionJobStatus`` field. If the status is ``COMPLETED`` , the job is finished and
        you can find the results at the location specified in the ``TranscriptionFileUri`` field.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/GetTranscriptionJob>`_

        **Request Syntax**
        ::

          response = client.get_transcription_job(
              TranscriptionJobName='string'
          )
        :type TranscriptionJobName: string
        :param TranscriptionJobName: **[REQUIRED]**

          The name of the job.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TranscriptionJob': {
                    'TranscriptionJobName': 'string',
                    'TranscriptionJobStatus': 'IN_PROGRESS'|'FAILED'|'COMPLETED',
                    'LanguageCode':
                    'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'
                    |'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'
                    |'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'
                    |'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
                    'MediaSampleRateHertz': 123,
                    'MediaFormat': 'mp3'|'mp4'|'wav'|'flac',
                    'Media': {
                        'MediaFileUri': 'string'
                    },
                    'Transcript': {
                        'TranscriptFileUri': 'string'
                    },
                    'CreationTime': datetime(2015, 1, 1),
                    'CompletionTime': datetime(2015, 1, 1),
                    'FailureReason': 'string',
                    'Settings': {
                        'VocabularyName': 'string',
                        'ShowSpeakerLabels': True|False,
                        'MaxSpeakerLabels': 123,
                        'ChannelIdentification': True|False,
                        'ShowAlternatives': True|False,
                        'MaxAlternatives': 123
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **TranscriptionJob** *(dict) --*

              An object that contains the results of the transcription job.

              - **TranscriptionJobName** *(string) --*

                The name of the transcription job.

              - **TranscriptionJobStatus** *(string) --*

                The status of the transcription job.

              - **LanguageCode** *(string) --*

                The language code for the input speech.

              - **MediaSampleRateHertz** *(integer) --*

                The sample rate, in Hertz, of the audio track in the input media file.

              - **MediaFormat** *(string) --*

                The format of the input media file.

              - **Media** *(dict) --*

                An object that describes the input media for the transcription job.

                - **MediaFileUri** *(string) --*

                  The S3 location of the input media file. The URI must be in the same region as the
                  API endpoint that you are calling. The general form is:

                   ``https://s3.<aws-region>.amazonaws.com/<bucket-name>/<keyprefix>/<objectkey>``

                  For example:

                   ``https://s3.us-east-1.amazonaws.com/examplebucket/example.mp4``

                   ``https://s3.us-east-1.amazonaws.com/examplebucket/mediadocs/example.mp4``

                  For more information about S3 object names, see `Object Keys
                  <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#object-keys>`__
                  in the *Amazon S3 Developer Guide* .

              - **Transcript** *(dict) --*

                An object that describes the output of the transcription job.

                - **TranscriptFileUri** *(string) --*

                  The location where the transcription is stored.

                  Use this URI to access the transcription. If you specified an S3 bucket in the
                  ``OutputBucketName`` field when you created the job, this is the URI of that
                  bucket. If you chose to store the transcription in Amazon Transcribe, this is a
                  shareable URL that provides secure access to that location.

              - **CreationTime** *(datetime) --*

                A timestamp that shows when the job was created.

              - **CompletionTime** *(datetime) --*

                A timestamp that shows when the job was completed.

              - **FailureReason** *(string) --*

                If the ``TranscriptionJobStatus`` field is ``FAILED`` , this field contains
                information about why the job failed.

                The ``FailureReason`` field can contain one of the following values:

                * ``Unsupported media format`` - The media format specified in the ``MediaFormat``
                field of the request isn't valid. See the description of the ``MediaFormat`` field
                for a list of valid values.

                * ``The media format provided does not match the detected media format`` - The media
                format of the audio file doesn't match the format specified in the ``MediaFormat``
                field in the request. Check the media format of your media file and make sure that
                the two values match.

                * ``Invalid sample rate for audio file`` - The sample rate specified in the
                ``MediaSampleRateHertz`` of the request isn't valid. The sample rate must be between
                8000 and 48000 Hertz.

                * ``The sample rate provided does not match the detected sample rate`` - The sample
                rate in the audio file doesn't match the sample rate specified in the
                ``MediaSampleRateHertz`` field in the request. Check the sample rate of your media
                file and make sure that the two values match.

                * ``Invalid file size: file size too large`` - The size of your audio file is larger
                than Amazon Transcribe can process. For more information, see `Limits
                <https://docs.aws.amazon.com/transcribe/latest/dg/limits-guidelines.html#limits>`__
                in the *Amazon Transcribe Developer Guide* .

                * ``Invalid number of channels: number of channels too large`` - Your audio contains
                more channels than Amazon Transcribe is configured to process. To request additional
                channels, see `Amazon Transcribe Limits
                <https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits-amazon-transcribe>`__
                in the *Amazon Web Services General Reference* .

              - **Settings** *(dict) --*

                Optional settings for the transcription job. Use these settings to turn on speaker
                recognition, to set the maximum number of speakers that should be identified and to
                specify a custom vocabulary to use when processing the transcription job.

                - **VocabularyName** *(string) --*

                  The name of a vocabulary to use when processing the transcription job.

                - **ShowSpeakerLabels** *(boolean) --*

                  Determines whether the transcription job uses speaker recognition to identify
                  different speakers in the input audio. Speaker recognition labels individual
                  speakers in the audio file. If you set the ``ShowSpeakerLabels`` field to true,
                  you must also set the maximum number of speaker labels ``MaxSpeakerLabels`` field.

                  You can't set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same
                  request. If you set both, your request returns a ``BadRequestException`` .

                - **MaxSpeakerLabels** *(integer) --*

                  The maximum number of speakers to identify in the input audio. If there are more
                  speakers in the audio than this number, multiple speakers will be identified as a
                  single speaker. If you specify the ``MaxSpeakerLabels`` field, you must set the
                  ``ShowSpeakerLabels`` field to true.

                - **ChannelIdentification** *(boolean) --*

                  Instructs Amazon Transcribe to process each audio channel separately and then
                  merge the transcription output of each channel into a single transcription.

                  Amazon Transcribe also produces a transcription of each item detected on an audio
                  channel, including the start time and end time of the item and alternative
                  transcriptions of the item including the confidence that Amazon Transcribe has in
                  the transcription.

                  You can't set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same
                  request. If you set both, your request returns a ``BadRequestException`` .

                - **ShowAlternatives** *(boolean) --*

                  Determines whether the transcription contains alternative transcriptions. If you
                  set the ``ShowAlternatives`` field to true, you must also set the maximum number
                  of alternatives to return in the ``MaxAlternatives`` field.

                - **MaxAlternatives** *(integer) --*

                  The number of alternative transcriptions that the service should return. If you
                  specify the ``MaxAlternatives`` field, you must set the ``ShowAlternatives`` field
                  to true.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_vocabulary(self, VocabularyName: str) -> ClientGetVocabularyResponseTypeDef:
        """
        Gets information about a vocabulary.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/GetVocabulary>`_

        **Request Syntax**
        ::

          response = client.get_vocabulary(
              VocabularyName='string'
          )
        :type VocabularyName: string
        :param VocabularyName: **[REQUIRED]**

          The name of the vocabulary to return information about. The name is case-sensitive.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'VocabularyName': 'string',
                'LanguageCode':
                'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'
                |'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'
                |'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'
                |'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
                'VocabularyState': 'PENDING'|'READY'|'FAILED',
                'LastModifiedTime': datetime(2015, 1, 1),
                'FailureReason': 'string',
                'DownloadUri': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **VocabularyName** *(string) --*

              The name of the vocabulary to return.

            - **LanguageCode** *(string) --*

              The language code of the vocabulary entries.

            - **VocabularyState** *(string) --*

              The processing state of the vocabulary.

            - **LastModifiedTime** *(datetime) --*

              The date and time that the vocabulary was last modified.

            - **FailureReason** *(string) --*

              If the ``VocabularyState`` field is ``FAILED`` , this field contains information about
              why the job failed.

            - **DownloadUri** *(string) --*

              The S3 location where the vocabulary is stored. Use this URI to get the contents of
              the vocabulary. The URI is available for a limited time.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_transcription_jobs(
        self,
        Status: Literal["IN_PROGRESS", "FAILED", "COMPLETED"] = None,
        JobNameContains: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListTranscriptionJobsResponseTypeDef:
        """
        Lists transcription jobs with the specified status.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/ListTranscriptionJobs>`_

        **Request Syntax**
        ::

          response = client.list_transcription_jobs(
              Status='IN_PROGRESS'|'FAILED'|'COMPLETED',
              JobNameContains='string',
              NextToken='string',
              MaxResults=123
          )
        :type Status: string
        :param Status:

          When specified, returns only transcription jobs with the specified status. Jobs are
          ordered by creation date, with the newest jobs returned first. If you don’t specify a
          status, Amazon Transcribe returns all transcription jobs ordered by creation date.

        :type JobNameContains: string
        :param JobNameContains:

          When specified, the jobs returned in the list are limited to jobs whose name contains the
          specified string.

        :type NextToken: string
        :param NextToken:

          If the result of the previous request to ``ListTranscriptionJobs`` was truncated, include
          the ``NextToken`` to fetch the next set of jobs.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of jobs to return in the response. If there are fewer results in the
          list, this response contains only the actual results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Status': 'IN_PROGRESS'|'FAILED'|'COMPLETED',
                'NextToken': 'string',
                'TranscriptionJobSummaries': [
                    {
                        'TranscriptionJobName': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'CompletionTime': datetime(2015, 1, 1),
                        'LanguageCode':
                        'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'
                        |'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'
                        |'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'
                        |'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'
                        |'ms-MY'|'ja-JP'|'ar-AE',
                        'TranscriptionJobStatus': 'IN_PROGRESS'|'FAILED'|'COMPLETED',
                        'FailureReason': 'string',
                        'OutputLocationType': 'CUSTOMER_BUCKET'|'SERVICE_BUCKET'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Status** *(string) --*

              The requested status of the jobs returned.

            - **NextToken** *(string) --*

              The ``ListTranscriptionJobs`` operation returns a page of jobs at a time. The maximum
              size of the page is set by the ``MaxResults`` parameter. If there are more jobs in the
              list than the page size, Amazon Transcribe returns the ``NextPage`` token. Include the
              token in the next request to the ``ListTranscriptionJobs`` operation to return in the
              next page of jobs.

            - **TranscriptionJobSummaries** *(list) --*

              A list of objects containing summary information for a transcription job.

              - *(dict) --*

                Provides a summary of information about a transcription job.

                - **TranscriptionJobName** *(string) --*

                  The name of the transcription job.

                - **CreationTime** *(datetime) --*

                  A timestamp that shows when the job was created.

                - **CompletionTime** *(datetime) --*

                  A timestamp that shows when the job was completed.

                - **LanguageCode** *(string) --*

                  The language code for the input speech.

                - **TranscriptionJobStatus** *(string) --*

                  The status of the transcription job. When the status is ``COMPLETED`` , use the
                  ``GetTranscriptionJob`` operation to get the results of the transcription.

                - **FailureReason** *(string) --*

                  If the ``TranscriptionJobStatus`` field is ``FAILED`` , a description of the
                  error.

                - **OutputLocationType** *(string) --*

                  Indicates the location of the output of the transcription job.

                  If the value is ``CUSTOMER_BUCKET`` then the location is the S3 bucket specified
                  in the ``outputBucketName`` field when the transcription job was started with the
                  ``StartTranscriptionJob`` operation.

                  If the value is ``SERVICE_BUCKET`` then the output is stored by Amazon Transcribe
                  and can be retrieved using the URI in the ``GetTranscriptionJob`` response's
                  ``TranscriptFileUri`` field.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_vocabularies(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        StateEquals: Literal["PENDING", "READY", "FAILED"] = None,
        NameContains: str = None,
    ) -> ClientListVocabulariesResponseTypeDef:
        """
        Returns a list of vocabularies that match the specified criteria. If no criteria are
        specified, returns the entire list of vocabularies.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/ListVocabularies>`_

        **Request Syntax**
        ::

          response = client.list_vocabularies(
              NextToken='string',
              MaxResults=123,
              StateEquals='PENDING'|'READY'|'FAILED',
              NameContains='string'
          )
        :type NextToken: string
        :param NextToken:

          If the result of the previous request to ``ListVocabularies`` was truncated, include the
          ``NextToken`` to fetch the next set of jobs.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of vocabularies to return in the response. If there are fewer results
          in the list, this response contains only the actual results.

        :type StateEquals: string
        :param StateEquals:

          When specified, only returns vocabularies with the ``VocabularyState`` field equal to the
          specified state.

        :type NameContains: string
        :param NameContains:

          When specified, the vocabularies returned in the list are limited to vocabularies whose
          name contains the specified string. The search is case-insensitive, ``ListVocabularies``
          will return both "vocabularyname" and "VocabularyName" in the response list.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Status': 'IN_PROGRESS'|'FAILED'|'COMPLETED',
                'NextToken': 'string',
                'Vocabularies': [
                    {
                        'VocabularyName': 'string',
                        'LanguageCode':
                        'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'
                        |'fr-FR'|'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'
                        |'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'
                        |'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'
                        |'ms-MY'|'ja-JP'|'ar-AE',
                        'LastModifiedTime': datetime(2015, 1, 1),
                        'VocabularyState': 'PENDING'|'READY'|'FAILED'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Status** *(string) --*

              The requested vocabulary state.

            - **NextToken** *(string) --*

              The ``ListVocabularies`` operation returns a page of vocabularies at a time. The
              maximum size of the page is set by the ``MaxResults`` parameter. If there are more
              jobs in the list than the page size, Amazon Transcribe returns the ``NextPage`` token.
              Include the token in the next request to the ``ListVocabularies`` operation to return
              in the next page of jobs.

            - **Vocabularies** *(list) --*

              A list of objects that describe the vocabularies that match the search criteria in the
              request.

              - *(dict) --*

                Provides information about a custom vocabulary.

                - **VocabularyName** *(string) --*

                  The name of the vocabulary.

                - **LanguageCode** *(string) --*

                  The language code of the vocabulary entries.

                - **LastModifiedTime** *(datetime) --*

                  The date and time that the vocabulary was last modified.

                - **VocabularyState** *(string) --*

                  The processing state of the vocabulary. If the state is ``READY`` you can use the
                  vocabulary in a ``StartTranscriptionJob`` request.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_transcription_job(
        self,
        TranscriptionJobName: str,
        LanguageCode: Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        Media: ClientStartTranscriptionJobMediaTypeDef,
        MediaSampleRateHertz: int = None,
        MediaFormat: Literal["mp3", "mp4", "wav", "flac"] = None,
        OutputBucketName: str = None,
        OutputEncryptionKMSKeyId: str = None,
        Settings: ClientStartTranscriptionJobSettingsTypeDef = None,
    ) -> ClientStartTranscriptionJobResponseTypeDef:
        """
        Starts an asynchronous job to transcribe speech to text.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/StartTranscriptionJob>`_

        **Request Syntax**
        ::

          response = client.start_transcription_job(
              TranscriptionJobName='string',
              LanguageCode=
                  'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'
                  |'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'
                  |'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'
                  |'ar-AE',
              MediaSampleRateHertz=123,
              MediaFormat='mp3'|'mp4'|'wav'|'flac',
              Media={
                  'MediaFileUri': 'string'
              },
              OutputBucketName='string',
              OutputEncryptionKMSKeyId='string',
              Settings={
                  'VocabularyName': 'string',
                  'ShowSpeakerLabels': True|False,
                  'MaxSpeakerLabels': 123,
                  'ChannelIdentification': True|False,
                  'ShowAlternatives': True|False,
                  'MaxAlternatives': 123
              }
          )
        :type TranscriptionJobName: string
        :param TranscriptionJobName: **[REQUIRED]**

          The name of the job. Note that you can't use the strings "." or ".." by themselves as the
          job name. The name must also be unique within an AWS account.

        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]**

          The language code for the language used in the input media file.

        :type MediaSampleRateHertz: integer
        :param MediaSampleRateHertz:

          The sample rate, in Hertz, of the audio track in the input media file.

          If you do not specify the media sample rate, Amazon Transcribe determines the sample rate.
          If you specify the sample rate, it must match the sample rate detected by Amazon
          Transcribe. In most cases, you should leave the ``MediaSampleRateHertz`` field blank and
          let Amazon Transcribe determine the sample rate.

        :type MediaFormat: string
        :param MediaFormat:

          The format of the input media file.

        :type Media: dict
        :param Media: **[REQUIRED]**

          An object that describes the input media for a transcription job.

          - **MediaFileUri** *(string) --*

            The S3 location of the input media file. The URI must be in the same region as the API
            endpoint that you are calling. The general form is:

             ``https://s3.<aws-region>.amazonaws.com/<bucket-name>/<keyprefix>/<objectkey>``

            For example:

             ``https://s3.us-east-1.amazonaws.com/examplebucket/example.mp4``

             ``https://s3.us-east-1.amazonaws.com/examplebucket/mediadocs/example.mp4``

            For more information about S3 object names, see `Object Keys
            <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#object-keys>`__ in
            the *Amazon S3 Developer Guide* .

        :type OutputBucketName: string
        :param OutputBucketName:

          The location where the transcription is stored.

          If you set the ``OutputBucketName`` , Amazon Transcribe puts the transcription in the
          specified S3 bucket. When you call the  GetTranscriptionJob operation, the operation
          returns this location in the ``TranscriptFileUri`` field. The S3 bucket must have
          permissions that allow Amazon Transcribe to put files in the bucket. For more information,
          see `Permissions Required for IAM User Roles
          <https://docs.aws.amazon.com/transcribe/latest/dg/security_iam_id-based-policy-examples.html#auth-role-iam-user>`__
          .

          You can specify an AWS Key Management Service (KMS) key to encrypt the output of your
          transcription using the ``OutputEncryptionKMSKeyId`` parameter. If you don't specify a KMS
          key, Amazon Transcribe uses the default Amazon S3 key for server-side encryption of
          transcripts that are placed in your S3 bucket.

          If you don't set the ``OutputBucketName`` , Amazon Transcribe generates a pre-signed URL,
          a shareable URL that provides secure access to your transcription, and returns it in the
          ``TranscriptFileUri`` field. Use this URL to download the transcription.

        :type OutputEncryptionKMSKeyId: string
        :param OutputEncryptionKMSKeyId:

          The Amazon Resource Name (ARN) of the AWS Key Management Service (KMS) key used to encrypt
          the output of the transcription job. The user calling the ``StartTranscriptionJob``
          operation must have permission to use the specified KMS key.

          You can use either of the following to identify a KMS key in the current account:

          * KMS Key ID: "1234abcd-12ab-34cd-56ef-1234567890ab"

          * KMS Key Alias: "alias/ExampleAlias"

          You can use either of the following to identify a KMS key in the current account or
          another account:

          * Amazon Resource Name (ARN) of a KMS Key: "arn:aws:kms:region:account
          ID:key/1234abcd-12ab-34cd-56ef-1234567890ab"

          * ARN of a KMS Key Alias: "arn:aws:kms:region:account ID:alias/ExampleAlias"

          If you don't specify an encryption key, the output of the transcription job is encrypted
          with the default Amazon S3 key (SSE-S3).

          If you specify a KMS key to encrypt your output, you must also specify an output location
          in the ``OutputBucketName`` parameter.

        :type Settings: dict
        :param Settings:

          A ``Settings`` object that provides optional settings for a transcription job.

          - **VocabularyName** *(string) --*

            The name of a vocabulary to use when processing the transcription job.

          - **ShowSpeakerLabels** *(boolean) --*

            Determines whether the transcription job uses speaker recognition to identify different
            speakers in the input audio. Speaker recognition labels individual speakers in the audio
            file. If you set the ``ShowSpeakerLabels`` field to true, you must also set the maximum
            number of speaker labels ``MaxSpeakerLabels`` field.

            You can't set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same
            request. If you set both, your request returns a ``BadRequestException`` .

          - **MaxSpeakerLabels** *(integer) --*

            The maximum number of speakers to identify in the input audio. If there are more
            speakers in the audio than this number, multiple speakers will be identified as a single
            speaker. If you specify the ``MaxSpeakerLabels`` field, you must set the
            ``ShowSpeakerLabels`` field to true.

          - **ChannelIdentification** *(boolean) --*

            Instructs Amazon Transcribe to process each audio channel separately and then merge the
            transcription output of each channel into a single transcription.

            Amazon Transcribe also produces a transcription of each item detected on an audio
            channel, including the start time and end time of the item and alternative
            transcriptions of the item including the confidence that Amazon Transcribe has in the
            transcription.

            You can't set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same
            request. If you set both, your request returns a ``BadRequestException`` .

          - **ShowAlternatives** *(boolean) --*

            Determines whether the transcription contains alternative transcriptions. If you set the
            ``ShowAlternatives`` field to true, you must also set the maximum number of alternatives
            to return in the ``MaxAlternatives`` field.

          - **MaxAlternatives** *(integer) --*

            The number of alternative transcriptions that the service should return. If you specify
            the ``MaxAlternatives`` field, you must set the ``ShowAlternatives`` field to true.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TranscriptionJob': {
                    'TranscriptionJobName': 'string',
                    'TranscriptionJobStatus': 'IN_PROGRESS'|'FAILED'|'COMPLETED',
                    'LanguageCode':
                    'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'
                    |'it-IT'|'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'
                    |'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'
                    |'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
                    'MediaSampleRateHertz': 123,
                    'MediaFormat': 'mp3'|'mp4'|'wav'|'flac',
                    'Media': {
                        'MediaFileUri': 'string'
                    },
                    'Transcript': {
                        'TranscriptFileUri': 'string'
                    },
                    'CreationTime': datetime(2015, 1, 1),
                    'CompletionTime': datetime(2015, 1, 1),
                    'FailureReason': 'string',
                    'Settings': {
                        'VocabularyName': 'string',
                        'ShowSpeakerLabels': True|False,
                        'MaxSpeakerLabels': 123,
                        'ChannelIdentification': True|False,
                        'ShowAlternatives': True|False,
                        'MaxAlternatives': 123
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **TranscriptionJob** *(dict) --*

              An object containing details of the asynchronous transcription job.

              - **TranscriptionJobName** *(string) --*

                The name of the transcription job.

              - **TranscriptionJobStatus** *(string) --*

                The status of the transcription job.

              - **LanguageCode** *(string) --*

                The language code for the input speech.

              - **MediaSampleRateHertz** *(integer) --*

                The sample rate, in Hertz, of the audio track in the input media file.

              - **MediaFormat** *(string) --*

                The format of the input media file.

              - **Media** *(dict) --*

                An object that describes the input media for the transcription job.

                - **MediaFileUri** *(string) --*

                  The S3 location of the input media file. The URI must be in the same region as the
                  API endpoint that you are calling. The general form is:

                   ``https://s3.<aws-region>.amazonaws.com/<bucket-name>/<keyprefix>/<objectkey>``

                  For example:

                   ``https://s3.us-east-1.amazonaws.com/examplebucket/example.mp4``

                   ``https://s3.us-east-1.amazonaws.com/examplebucket/mediadocs/example.mp4``

                  For more information about S3 object names, see `Object Keys
                  <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#object-keys>`__
                  in the *Amazon S3 Developer Guide* .

              - **Transcript** *(dict) --*

                An object that describes the output of the transcription job.

                - **TranscriptFileUri** *(string) --*

                  The location where the transcription is stored.

                  Use this URI to access the transcription. If you specified an S3 bucket in the
                  ``OutputBucketName`` field when you created the job, this is the URI of that
                  bucket. If you chose to store the transcription in Amazon Transcribe, this is a
                  shareable URL that provides secure access to that location.

              - **CreationTime** *(datetime) --*

                A timestamp that shows when the job was created.

              - **CompletionTime** *(datetime) --*

                A timestamp that shows when the job was completed.

              - **FailureReason** *(string) --*

                If the ``TranscriptionJobStatus`` field is ``FAILED`` , this field contains
                information about why the job failed.

                The ``FailureReason`` field can contain one of the following values:

                * ``Unsupported media format`` - The media format specified in the ``MediaFormat``
                field of the request isn't valid. See the description of the ``MediaFormat`` field
                for a list of valid values.

                * ``The media format provided does not match the detected media format`` - The media
                format of the audio file doesn't match the format specified in the ``MediaFormat``
                field in the request. Check the media format of your media file and make sure that
                the two values match.

                * ``Invalid sample rate for audio file`` - The sample rate specified in the
                ``MediaSampleRateHertz`` of the request isn't valid. The sample rate must be between
                8000 and 48000 Hertz.

                * ``The sample rate provided does not match the detected sample rate`` - The sample
                rate in the audio file doesn't match the sample rate specified in the
                ``MediaSampleRateHertz`` field in the request. Check the sample rate of your media
                file and make sure that the two values match.

                * ``Invalid file size: file size too large`` - The size of your audio file is larger
                than Amazon Transcribe can process. For more information, see `Limits
                <https://docs.aws.amazon.com/transcribe/latest/dg/limits-guidelines.html#limits>`__
                in the *Amazon Transcribe Developer Guide* .

                * ``Invalid number of channels: number of channels too large`` - Your audio contains
                more channels than Amazon Transcribe is configured to process. To request additional
                channels, see `Amazon Transcribe Limits
                <https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits-amazon-transcribe>`__
                in the *Amazon Web Services General Reference* .

              - **Settings** *(dict) --*

                Optional settings for the transcription job. Use these settings to turn on speaker
                recognition, to set the maximum number of speakers that should be identified and to
                specify a custom vocabulary to use when processing the transcription job.

                - **VocabularyName** *(string) --*

                  The name of a vocabulary to use when processing the transcription job.

                - **ShowSpeakerLabels** *(boolean) --*

                  Determines whether the transcription job uses speaker recognition to identify
                  different speakers in the input audio. Speaker recognition labels individual
                  speakers in the audio file. If you set the ``ShowSpeakerLabels`` field to true,
                  you must also set the maximum number of speaker labels ``MaxSpeakerLabels`` field.

                  You can't set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same
                  request. If you set both, your request returns a ``BadRequestException`` .

                - **MaxSpeakerLabels** *(integer) --*

                  The maximum number of speakers to identify in the input audio. If there are more
                  speakers in the audio than this number, multiple speakers will be identified as a
                  single speaker. If you specify the ``MaxSpeakerLabels`` field, you must set the
                  ``ShowSpeakerLabels`` field to true.

                - **ChannelIdentification** *(boolean) --*

                  Instructs Amazon Transcribe to process each audio channel separately and then
                  merge the transcription output of each channel into a single transcription.

                  Amazon Transcribe also produces a transcription of each item detected on an audio
                  channel, including the start time and end time of the item and alternative
                  transcriptions of the item including the confidence that Amazon Transcribe has in
                  the transcription.

                  You can't set both ``ShowSpeakerLabels`` and ``ChannelIdentification`` in the same
                  request. If you set both, your request returns a ``BadRequestException`` .

                - **ShowAlternatives** *(boolean) --*

                  Determines whether the transcription contains alternative transcriptions. If you
                  set the ``ShowAlternatives`` field to true, you must also set the maximum number
                  of alternatives to return in the ``MaxAlternatives`` field.

                - **MaxAlternatives** *(integer) --*

                  The number of alternative transcriptions that the service should return. If you
                  specify the ``MaxAlternatives`` field, you must set the ``ShowAlternatives`` field
                  to true.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_vocabulary(
        self,
        VocabularyName: str,
        LanguageCode: Literal[
            "en-US",
            "es-US",
            "en-AU",
            "fr-CA",
            "en-GB",
            "de-DE",
            "pt-BR",
            "fr-FR",
            "it-IT",
            "ko-KR",
            "es-ES",
            "en-IN",
            "hi-IN",
            "ar-SA",
            "ru-RU",
            "zh-CN",
            "nl-NL",
            "id-ID",
            "ta-IN",
            "fa-IR",
            "en-IE",
            "en-AB",
            "en-WL",
            "pt-PT",
            "te-IN",
            "tr-TR",
            "de-CH",
            "he-IL",
            "ms-MY",
            "ja-JP",
            "ar-AE",
        ],
        Phrases: List[str] = None,
        VocabularyFileUri: str = None,
    ) -> ClientUpdateVocabularyResponseTypeDef:
        """
        Updates an existing vocabulary with new values. The ``UpdateVocabulary`` operation
        overwrites all of the existing information with the values that you provide in the request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/UpdateVocabulary>`_

        **Request Syntax**
        ::

          response = client.update_vocabulary(
              VocabularyName='string',
              LanguageCode=
                  'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'|'ko-KR'
                  |'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'|'ta-IN'|'fa-IR'
                  |'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'|'he-IL'|'ms-MY'|'ja-JP'
                  |'ar-AE',
              Phrases=[
                  'string',
              ],
              VocabularyFileUri='string'
          )
        :type VocabularyName: string
        :param VocabularyName: **[REQUIRED]**

          The name of the vocabulary to update. The name is case-sensitive.

        :type LanguageCode: string
        :param LanguageCode: **[REQUIRED]**

          The language code of the vocabulary entries.

        :type Phrases: list
        :param Phrases:

          An array of strings containing the vocabulary entries.

          - *(string) --*

        :type VocabularyFileUri: string
        :param VocabularyFileUri:

          The S3 location of the text file that contains the definition of the custom vocabulary.
          The URI must be in the same region as the API endpoint that you are calling. The general
          form is

           ``https://s3.<aws-region>.amazonaws.com/<bucket-name>/<keyprefix>/<objectkey>``

          For example:

           ``https://s3.us-east-1.amazonaws.com/examplebucket/vocab.txt``

          For more information about S3 object names, see `Object Keys
          <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#object-keys>`__ in the
          *Amazon S3 Developer Guide* .

          For more information about custom vocabularies, see `Custom Vocabularies
          <http://docs.aws.amazon.com/transcribe/latest/dg/how-it-works.html#how-vocabulary>`__ .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'VocabularyName': 'string',
                'LanguageCode':
                'en-US'|'es-US'|'en-AU'|'fr-CA'|'en-GB'|'de-DE'|'pt-BR'|'fr-FR'|'it-IT'
                |'ko-KR'|'es-ES'|'en-IN'|'hi-IN'|'ar-SA'|'ru-RU'|'zh-CN'|'nl-NL'|'id-ID'
                |'ta-IN'|'fa-IR'|'en-IE'|'en-AB'|'en-WL'|'pt-PT'|'te-IN'|'tr-TR'|'de-CH'
                |'he-IL'|'ms-MY'|'ja-JP'|'ar-AE',
                'LastModifiedTime': datetime(2015, 1, 1),
                'VocabularyState': 'PENDING'|'READY'|'FAILED'
            }
          **Response Structure**

          - *(dict) --*

            - **VocabularyName** *(string) --*

              The name of the vocabulary that was updated.

            - **LanguageCode** *(string) --*

              The language code of the vocabulary entries.

            - **LastModifiedTime** *(datetime) --*

              The date and time that the vocabulary was updated.

            - **VocabularyState** *(string) --*

              The processing state of the vocabulary. When the ``VocabularyState`` field contains
              ``READY`` the vocabulary is ready to be used in a ``StartTranscriptionJob`` request.
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    InternalFailureException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotFoundException: Boto3ClientError
