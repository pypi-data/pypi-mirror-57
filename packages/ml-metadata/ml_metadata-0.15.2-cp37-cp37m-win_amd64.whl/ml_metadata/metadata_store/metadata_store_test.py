# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for ml_metadata.metadata_store.metadata_store."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
from absl.testing import absltest
import grpc

from ml_metadata.metadata_store import metadata_store
from ml_metadata.proto import metadata_store_pb2
from tensorflow.python.framework import errors


def _get_metadata_store():
  connection_config = metadata_store_pb2.ConnectionConfig()
  connection_config.sqlite.SetInParent()
  return metadata_store.MetadataStore(connection_config)


def _create_example_artifact_type():
  artifact_type = metadata_store_pb2.ArtifactType()
  artifact_type.name = "test_type_1"
  artifact_type.properties["foo"] = metadata_store_pb2.INT
  artifact_type.properties["bar"] = metadata_store_pb2.STRING
  artifact_type.properties["baz"] = metadata_store_pb2.DOUBLE
  return artifact_type


def _create_example_artifact_type_2():
  artifact_type = metadata_store_pb2.ArtifactType()
  artifact_type.name = "test_type_2"
  artifact_type.properties["foo"] = metadata_store_pb2.INT
  artifact_type.properties["bar"] = metadata_store_pb2.STRING
  artifact_type.properties["baz"] = metadata_store_pb2.DOUBLE
  return artifact_type


def _create_example_execution_type():
  execution_type = metadata_store_pb2.ExecutionType()
  execution_type.name = "test_type_1"
  execution_type.properties["foo"] = metadata_store_pb2.INT
  execution_type.properties["bar"] = metadata_store_pb2.STRING
  return execution_type


def _create_example_execution_type_2():
  execution_type = metadata_store_pb2.ExecutionType()
  execution_type.name = "test_type_2"
  execution_type.properties["foo"] = metadata_store_pb2.INT
  execution_type.properties["bar"] = metadata_store_pb2.STRING
  return execution_type


def _create_example_context_type():
  context_type = metadata_store_pb2.ContextType()
  context_type.name = "test_type_1"
  context_type.properties["foo"] = metadata_store_pb2.INT
  context_type.properties["bar"] = metadata_store_pb2.STRING
  context_type.properties["baz"] = metadata_store_pb2.DOUBLE
  return context_type


def _create_example_context_type_2():
  context_type = metadata_store_pb2.ContextType()
  context_type.name = "test_type_2"
  context_type.properties["foo"] = metadata_store_pb2.INT
  context_type.properties["bar"] = metadata_store_pb2.STRING
  return context_type


def _create_grpc_error_with_code(error_code):
  e = grpc.RpcError()
  e.code = lambda: error_code
  e.details = lambda: "mock_error"
  raise e


class MetadataStoreTest(absltest.TestCase):

  def test_unset_connection_config(self):
    connection_config = metadata_store_pb2.ConnectionConfig()
    for _ in range(3):
      with self.assertRaises(RuntimeError):
        metadata_store.MetadataStore(connection_config)

  def test_put_artifact_type_get_artifact_type(self):
    store = _get_metadata_store()
    artifact_type = _create_example_artifact_type()

    type_id = store.put_artifact_type(artifact_type)
    artifact_type_result = store.get_artifact_type("test_type_1")
    self.assertEqual(artifact_type_result.id, type_id)
    self.assertEqual(artifact_type_result.name, "test_type_1")
    self.assertEqual(artifact_type_result.properties["foo"],
                     metadata_store_pb2.INT)
    self.assertEqual(artifact_type_result.properties["bar"],
                     metadata_store_pb2.STRING)
    self.assertEqual(artifact_type_result.properties["baz"],
                     metadata_store_pb2.DOUBLE)

  def test_put_artifact_type_with_update_get_artifact_type(self):
    store = _get_metadata_store()
    artifact_type = _create_example_artifact_type()
    type_id = store.put_artifact_type(artifact_type)

    artifact_type.properties["new_property"] = metadata_store_pb2.INT
    store.put_artifact_type(artifact_type, can_add_fields=True)

    artifact_type_result = store.get_artifact_type("test_type_1")
    self.assertEqual(artifact_type_result.id, type_id)
    self.assertEqual(artifact_type_result.name, "test_type_1")
    self.assertEqual(artifact_type_result.properties["foo"],
                     metadata_store_pb2.INT)
    self.assertEqual(artifact_type_result.properties["bar"],
                     metadata_store_pb2.STRING)
    self.assertEqual(artifact_type.properties["baz"], metadata_store_pb2.DOUBLE)
    self.assertEqual(artifact_type.properties["new_property"],
                     metadata_store_pb2.INT)

  def test_get_artifact_types(self):
    store = _get_metadata_store()
    artifact_type_1 = _create_example_artifact_type()
    artifact_type_2 = _create_example_artifact_type_2()

    type_id_1 = store.put_artifact_type(artifact_type_1)
    artifact_type_1.id = type_id_1
    type_id_2 = store.put_artifact_type(artifact_type_2)
    artifact_type_2.id = type_id_2

    got_types = store.get_artifact_types()
    got_types.sort(key=lambda x: x.id)
    self.assertListEqual([artifact_type_1, artifact_type_2], got_types)

  def test_get_execution_types(self):
    store = _get_metadata_store()
    execution_type_1 = _create_example_execution_type()
    execution_type_2 = _create_example_execution_type_2()

    type_id_1 = store.put_execution_type(execution_type_1)
    execution_type_1.id = type_id_1
    type_id_2 = store.put_execution_type(execution_type_2)
    execution_type_2.id = type_id_2

    got_types = store.get_execution_types()
    got_types.sort(key=lambda x: x.id)
    self.assertListEqual([execution_type_1, execution_type_2], got_types)

  def test_get_context_types(self):
    store = _get_metadata_store()
    context_type_1 = _create_example_context_type()
    context_type_2 = _create_example_context_type_2()

    type_id_1 = store.put_context_type(context_type_1)
    context_type_1.id = type_id_1
    type_id_2 = store.put_context_type(context_type_2)
    context_type_2.id = type_id_2

    got_types = store.get_context_types()
    got_types.sort(key=lambda x: x.id)
    self.assertListEqual([context_type_1, context_type_2], got_types)

  def test_put_artifacts_get_artifacts_by_id(self):
    store = _get_metadata_store()
    artifact_type = _create_example_artifact_type()
    type_id = store.put_artifact_type(artifact_type)
    artifact = metadata_store_pb2.Artifact()
    artifact.type_id = type_id
    artifact.properties["foo"].int_value = 3
    artifact.properties["bar"].string_value = "Hello"
    [artifact_id] = store.put_artifacts([artifact])
    [artifact_result] = store.get_artifacts_by_id([artifact_id])
    self.assertEqual(artifact_result.properties["bar"].string_value, "Hello")
    self.assertEqual(artifact_result.properties["foo"].int_value, 3)

  def test_put_artifacts_get_artifacts(self):
    store = _get_metadata_store()
    artifact_type = _create_example_artifact_type()
    type_id = store.put_artifact_type(artifact_type)
    artifact_0 = metadata_store_pb2.Artifact()
    artifact_0.type_id = type_id
    artifact_0.properties["foo"].int_value = 3
    artifact_0.properties["bar"].string_value = "Hello"
    artifact_1 = metadata_store_pb2.Artifact()
    artifact_1.type_id = type_id

    [artifact_id_0,
     artifact_id_1] = store.put_artifacts([artifact_0, artifact_1])
    artifact_result = store.get_artifacts()
    if artifact_result[0].id == artifact_id_0:
      [artifact_result_0, artifact_result_1] = artifact_result
    else:
      [artifact_result_1, artifact_result_0] = artifact_result
    self.assertEqual(artifact_result_0.id, artifact_id_0)
    self.assertEqual(artifact_result_0.properties["bar"].string_value, "Hello")
    self.assertEqual(artifact_result_0.properties["foo"].int_value, 3)
    self.assertEqual(artifact_result_1.id, artifact_id_1)

  def test_put_artifacts_get_artifacts_by_type(self):
    store = _get_metadata_store()
    artifact_type = _create_example_artifact_type()
    type_id = store.put_artifact_type(artifact_type)
    artifact_type_2 = _create_example_artifact_type_2()
    type_id_2 = store.put_artifact_type(artifact_type_2)
    artifact_0 = metadata_store_pb2.Artifact()
    artifact_0.type_id = type_id
    artifact_0.properties["foo"].int_value = 3
    artifact_0.properties["bar"].string_value = "Hello"
    artifact_1 = metadata_store_pb2.Artifact()
    artifact_1.type_id = type_id_2

    [_, artifact_id_1] = store.put_artifacts([artifact_0, artifact_1])
    artifact_result = store.get_artifacts_by_type(artifact_type_2.name)
    self.assertLen(artifact_result, 1)
    self.assertEqual(artifact_result[0].id, artifact_id_1)

  def test_put_artifacts_get_artifacts_by_uri(self):
    store = _get_metadata_store()
    artifact_type = _create_example_artifact_type()
    type_id = store.put_artifact_type(artifact_type)
    want_artifact = metadata_store_pb2.Artifact()
    want_artifact.type_id = type_id
    want_artifact.uri = "test_uri"
    other_artifact = metadata_store_pb2.Artifact()
    other_artifact.uri = "other_uri"
    other_artifact.type_id = type_id

    [want_artifact_id, _] = store.put_artifacts([want_artifact, other_artifact])
    artifact_result = store.get_artifacts_by_uri(want_artifact.uri)
    self.assertLen(artifact_result, 1)
    self.assertEqual(artifact_result[0].id, want_artifact_id)

  def test_put_executions_get_executions_by_type(self):
    store = _get_metadata_store()
    execution_type = _create_example_execution_type()
    type_id = store.put_execution_type(execution_type)
    execution_type_2 = _create_example_execution_type_2()
    type_id_2 = store.put_execution_type(execution_type_2)
    execution_0 = metadata_store_pb2.Execution()
    execution_0.type_id = type_id
    execution_0.properties["foo"].int_value = 3
    execution_0.properties["bar"].string_value = "Hello"
    execution_1 = metadata_store_pb2.Execution()
    execution_1.type_id = type_id_2

    [_, execution_id_1] = store.put_executions([execution_0, execution_1])
    execution_result = store.get_executions_by_type(execution_type_2.name)
    self.assertLen(execution_result, 1)
    self.assertEqual(execution_result[0].id, execution_id_1)

  def test_update_artifact_get_artifact(self):
    store = _get_metadata_store()
    artifact_type = _create_example_artifact_type()
    type_id = store.put_artifact_type(artifact_type)
    artifact = metadata_store_pb2.Artifact()
    artifact.type_id = type_id
    artifact.properties["bar"].string_value = "Hello"

    [artifact_id] = store.put_artifacts([artifact])
    artifact_2 = metadata_store_pb2.Artifact()
    artifact_2.CopyFrom(artifact)
    artifact_2.id = artifact_id
    artifact_2.properties["foo"].int_value = artifact_id
    artifact_2.properties["bar"].string_value = "Goodbye"
    [artifact_id_2] = store.put_artifacts([artifact_2])
    self.assertEqual(artifact_id, artifact_id_2)

    [artifact_result] = store.get_artifacts_by_id([artifact_id])
    self.assertEqual(artifact_result.properties["bar"].string_value, "Goodbye")
    self.assertEqual(artifact_result.properties["foo"].int_value, artifact_id)

  def test_create_artifact_with_type_get_artifacts_by_id(self):
    store = _get_metadata_store()
    artifact_type = _create_example_artifact_type()
    artifact = metadata_store_pb2.Artifact()
    artifact.properties["foo"].int_value = 3
    artifact.properties["bar"].string_value = "Hello"
    artifact_id = store.create_artifact_with_type(artifact, artifact_type)
    [artifact_result] = store.get_artifacts_by_id([artifact_id])
    self.assertEqual(artifact_result.properties["bar"].string_value, "Hello")
    self.assertEqual(artifact_result.properties["foo"].int_value, 3)

  def test_put_execution_type_get_execution_type(self):
    store = _get_metadata_store()
    execution_type = metadata_store_pb2.ExecutionType()
    execution_type.name = "test_type_1"
    execution_type.properties["foo"] = metadata_store_pb2.INT
    execution_type.properties["bar"] = metadata_store_pb2.STRING
    type_id = store.put_execution_type(execution_type)
    execution_type_result = store.get_execution_type("test_type_1")
    self.assertEqual(execution_type_result.id, type_id)
    self.assertEqual(execution_type_result.name, "test_type_1")

  def test_put_execution_type_with_update_get_execution_type(self):
    store = _get_metadata_store()
    execution_type = metadata_store_pb2.ExecutionType()
    execution_type.name = "test_type"
    execution_type.properties["foo"] = metadata_store_pb2.DOUBLE
    type_id = store.put_execution_type(execution_type)

    want_execution_type = metadata_store_pb2.ExecutionType()
    want_execution_type.id = type_id
    want_execution_type.name = "test_type"
    want_execution_type.properties["foo"] = metadata_store_pb2.DOUBLE
    want_execution_type.properties["new_property"] = metadata_store_pb2.INT
    store.put_execution_type(want_execution_type, can_add_fields=True)

    got_execution_type = store.get_execution_type("test_type")
    self.assertEqual(got_execution_type.id, type_id)
    self.assertEqual(got_execution_type.name, "test_type")
    self.assertEqual(got_execution_type.properties["foo"],
                     metadata_store_pb2.DOUBLE)
    self.assertEqual(got_execution_type.properties["new_property"],
                     metadata_store_pb2.INT)

  def test_put_executions_get_executions_by_id(self):
    store = _get_metadata_store()
    execution_type = metadata_store_pb2.ExecutionType()
    execution_type.name = "test_type_1"
    execution_type.properties["foo"] = metadata_store_pb2.INT
    execution_type.properties["bar"] = metadata_store_pb2.STRING
    type_id = store.put_execution_type(execution_type)
    execution = metadata_store_pb2.Execution()
    execution.type_id = type_id
    execution.properties["foo"].int_value = 3
    execution.properties["bar"].string_value = "Hello"
    [execution_id] = store.put_executions([execution])
    [execution_result] = store.get_executions_by_id([execution_id])
    self.assertEqual(execution_result.properties["bar"].string_value, "Hello")
    self.assertEqual(execution_result.properties["foo"].int_value, 3)

  def test_put_executions_get_executions(self):
    store = _get_metadata_store()
    execution_type = _create_example_execution_type()
    type_id = store.put_execution_type(execution_type)
    execution_0 = metadata_store_pb2.Execution()
    execution_0.type_id = type_id
    execution_0.properties["foo"].int_value = 3
    execution_0.properties["bar"].string_value = "Hello"
    execution_1 = metadata_store_pb2.Execution()
    execution_1.type_id = type_id
    execution_1.properties["foo"].int_value = -9
    execution_1.properties["bar"].string_value = "Goodbye"

    [execution_id_0,
     execution_id_1] = store.put_executions([execution_0, execution_1])

    execution_result = store.get_executions()
    self.assertLen(execution_result, 2)
    # Normalize the order of the results.
    if execution_result[0].id == execution_id_0:
      [execution_result_0, execution_result_1] = execution_result
    else:
      [execution_result_1, execution_result_0] = execution_result

    self.assertEqual(execution_result_0.id, execution_id_0)
    self.assertEqual(execution_result_0.properties["bar"].string_value, "Hello")
    self.assertEqual(execution_result_0.properties["foo"].int_value, 3)
    self.assertEqual(execution_result_1.id, execution_id_1)
    self.assertEqual(execution_result_1.properties["bar"].string_value,
                     "Goodbye")
    self.assertEqual(execution_result_1.properties["foo"].int_value, -9)

  def test_update_execution_get_execution(self):
    store = _get_metadata_store()
    execution_type = metadata_store_pb2.ExecutionType()
    execution_type.name = "test_type_1"
    execution_type.properties["foo"] = metadata_store_pb2.INT
    execution_type.properties["bar"] = metadata_store_pb2.STRING
    type_id = store.put_execution_type(execution_type)
    execution = metadata_store_pb2.Execution()
    execution.type_id = type_id
    execution.properties["bar"].string_value = "Hello"

    [execution_id] = store.put_executions([execution])
    execution_2 = metadata_store_pb2.Execution()
    execution_2.id = execution_id
    execution_2.type_id = type_id
    execution_2.properties["foo"].int_value = 12
    execution_2.properties["bar"].string_value = "Goodbye"
    [execution_id_2] = store.put_executions([execution_2])
    self.assertEqual(execution_id, execution_id_2)

    [execution_result] = store.get_executions_by_id([execution_id])
    self.assertEqual(execution_result.properties["bar"].string_value, "Goodbye")
    self.assertEqual(execution_result.properties["foo"].int_value, 12)

  def test_put_events_get_events(self):
    store = _get_metadata_store()
    execution_type = metadata_store_pb2.ExecutionType()
    execution_type.name = "execution_type"
    execution_type_id = store.put_execution_type(execution_type)
    execution = metadata_store_pb2.Execution()
    execution.type_id = execution_type_id
    [execution_id] = store.put_executions([execution])
    artifact_type = metadata_store_pb2.ArtifactType()
    artifact_type.name = "artifact_type"
    artifact_type_id = store.put_artifact_type(artifact_type)
    artifact = metadata_store_pb2.Artifact()
    artifact.type_id = artifact_type_id
    [artifact_id] = store.put_artifacts([artifact])

    event = metadata_store_pb2.Event()
    event.type = metadata_store_pb2.Event.DECLARED_OUTPUT
    event.artifact_id = artifact_id
    event.execution_id = execution_id
    store.put_events([event])
    [event_result] = store.get_events_by_artifact_ids([artifact_id])
    self.assertEqual(event_result.artifact_id, artifact_id)
    self.assertEqual(event_result.execution_id, execution_id)
    self.assertEqual(event_result.type,
                     metadata_store_pb2.Event.DECLARED_OUTPUT)

    [event_result_2] = store.get_events_by_execution_ids([execution_id])
    self.assertEqual(event_result_2.artifact_id, artifact_id)
    self.assertEqual(event_result_2.execution_id, execution_id)
    self.assertEqual(event_result_2.type,
                     metadata_store_pb2.Event.DECLARED_OUTPUT)

  def test_get_executions_by_id_empty(self):
    store = _get_metadata_store()
    result = store.get_executions_by_id({})
    self.assertEmpty(result)

  def test_get_artifact_type_fails(self):
    store = _get_metadata_store()
    with self.assertRaises(errors.NotFoundError):
      store.get_artifact_type("test_type_1")

  def test_put_events_no_artifact_id(self):
    # No execution_id throws the same error type, so we just test this.
    store = _get_metadata_store()
    execution_type = metadata_store_pb2.ExecutionType()
    execution_type.name = "execution_type"
    execution_type_id = store.put_execution_type(execution_type)
    execution = metadata_store_pb2.Execution()
    execution.type_id = execution_type_id
    [execution_id] = store.put_executions([execution])

    event = metadata_store_pb2.Event()
    event.type = metadata_store_pb2.Event.DECLARED_OUTPUT
    event.execution_id = execution_id
    with self.assertRaises(errors.InvalidArgumentError):
      store.put_events([event])

  def test_put_events_with_paths(self):
    store = _get_metadata_store()
    execution_type = metadata_store_pb2.ExecutionType()
    execution_type.name = "execution_type"
    execution_type_id = store.put_execution_type(execution_type)
    execution = metadata_store_pb2.Execution()
    execution.type_id = execution_type_id
    [execution_id] = store.put_executions([execution])
    artifact_type = metadata_store_pb2.ArtifactType()
    artifact_type.name = "artifact_type"
    artifact_type_id = store.put_artifact_type(artifact_type)
    artifact_0 = metadata_store_pb2.Artifact()
    artifact_0.type_id = artifact_type_id
    artifact_1 = metadata_store_pb2.Artifact()
    artifact_1.type_id = artifact_type_id
    [artifact_id_0,
     artifact_id_1] = store.put_artifacts([artifact_0, artifact_1])

    event_0 = metadata_store_pb2.Event()
    event_0.type = metadata_store_pb2.Event.DECLARED_INPUT
    event_0.artifact_id = artifact_id_0
    event_0.execution_id = execution_id
    event_0.path.steps.add().key = "ggg"

    event_1 = metadata_store_pb2.Event()
    event_1.type = metadata_store_pb2.Event.DECLARED_INPUT
    event_1.artifact_id = artifact_id_1
    event_1.execution_id = execution_id
    event_1.path.steps.add().key = "fff"

    store.put_events([event_0, event_1])
    [event_result_0,
     event_result_1] = store.get_events_by_execution_ids([execution_id])
    self.assertLen(event_result_0.path.steps, 1)
    self.assertEqual(event_result_0.path.steps[0].key, "ggg")
    self.assertLen(event_result_1.path.steps, 1)
    self.assertEqual(event_result_1.path.steps[0].key, "fff")

  def test_put_events_with_paths_same_artifact(self):
    store = _get_metadata_store()
    execution_type = metadata_store_pb2.ExecutionType()
    execution_type.name = "execution_type"
    execution_type_id = store.put_execution_type(execution_type)
    execution_0 = metadata_store_pb2.Execution()
    execution_0.type_id = execution_type_id
    execution_1 = metadata_store_pb2.Execution()
    execution_1.type_id = execution_type_id
    [execution_id_0,
     execution_id_1] = store.put_executions([execution_0, execution_1])
    artifact_type = metadata_store_pb2.ArtifactType()
    artifact_type.name = "artifact_type"
    artifact_type_id = store.put_artifact_type(artifact_type)
    artifact = metadata_store_pb2.Artifact()
    artifact.type_id = artifact_type_id
    [artifact_id] = store.put_artifacts([artifact])

    event_0 = metadata_store_pb2.Event()
    event_0.type = metadata_store_pb2.Event.DECLARED_INPUT
    event_0.artifact_id = artifact_id
    event_0.execution_id = execution_id_0
    event_0.path.steps.add().key = "ggg"

    event_1 = metadata_store_pb2.Event()
    event_1.type = metadata_store_pb2.Event.DECLARED_INPUT
    event_1.artifact_id = artifact_id
    event_1.execution_id = execution_id_1
    event_1.path.steps.add().key = "fff"

    store.put_events([event_0, event_1])
    [event_result_0,
     event_result_1] = store.get_events_by_artifact_ids([artifact_id])
    self.assertLen(event_result_0.path.steps, 1)
    self.assertEqual(event_result_0.path.steps[0].key, "ggg")
    self.assertLen(event_result_1.path.steps, 1)
    self.assertEqual(event_result_1.path.steps[0].key, "fff")

  def test_publish_execution(self):
    store = _get_metadata_store()
    execution_type = metadata_store_pb2.ExecutionType()
    execution_type.name = "execution_type"
    execution_type_id = store.put_execution_type(execution_type)
    execution = metadata_store_pb2.Execution()
    execution.type_id = execution_type_id

    artifact_type = metadata_store_pb2.ArtifactType()
    artifact_type.name = "artifact_type"
    artifact_type_id = store.put_artifact_type(artifact_type)
    input_artifact = metadata_store_pb2.Artifact()
    input_artifact.type_id = artifact_type_id
    output_artifact = metadata_store_pb2.Artifact()
    output_artifact.type_id = artifact_type_id
    output_event = metadata_store_pb2.Event()
    output_event.type = metadata_store_pb2.Event.DECLARED_INPUT

    execution_id, artifact_ids = store.put_execution(
        execution, [[input_artifact], [output_artifact, output_event]])
    self.assertLen(artifact_ids, 2)
    events = store.get_events_by_execution_ids([execution_id])
    self.assertLen(events, 1)

  def test_put_context_type_get_context_type(self):
    store = _get_metadata_store()
    context_type = _create_example_context_type()

    type_id = store.put_context_type(context_type)
    context_type_result = store.get_context_type("test_type_1")
    self.assertEqual(context_type_result.id, type_id)
    self.assertEqual(context_type_result.name, "test_type_1")

    context_types_by_id_results = store.get_context_types_by_id([type_id])
    self.assertLen(context_types_by_id_results, 1)
    self.assertEqual(context_types_by_id_results[0].id, type_id)
    self.assertEqual(context_types_by_id_results[0].name, "test_type_1")

  def test_put_context_type_with_update_get_context_type(self):
    store = _get_metadata_store()
    context_type = metadata_store_pb2.ContextType()
    context_type.name = "test_type"
    context_type.properties["foo"] = metadata_store_pb2.INT
    type_id = store.put_context_type(context_type)

    want_context_type = metadata_store_pb2.ContextType()
    want_context_type.name = "test_type"
    want_context_type.properties["foo"] = metadata_store_pb2.INT
    want_context_type.properties["new_property"] = metadata_store_pb2.STRING
    store.put_context_type(want_context_type, can_add_fields=True)

    got_context_type = store.get_context_type("test_type")
    self.assertEqual(got_context_type.id, type_id)
    self.assertEqual(got_context_type.name, "test_type")
    self.assertEqual(got_context_type.properties["foo"], metadata_store_pb2.INT)
    self.assertEqual(got_context_type.properties["new_property"],
                     metadata_store_pb2.STRING)

  def test_put_contexts_get_contexts_by_id(self):
    store = _get_metadata_store()
    context_type = _create_example_context_type()
    type_id = store.put_context_type(context_type)
    context = metadata_store_pb2.Context()
    context.type_id = type_id
    context.name = "context1"
    context.properties["foo"].int_value = 3
    context.custom_properties["abc"].string_value = "s"
    [context_id] = store.put_contexts([context])
    [context_result] = store.get_contexts_by_id([context_id])
    self.assertEqual(context_result.name, context.name)
    self.assertEqual(context_result.properties["foo"].int_value,
                     context.properties["foo"].int_value)
    self.assertEqual(context_result.custom_properties["abc"].string_value,
                     context.custom_properties["abc"].string_value)

  def test_put_contexts_get_contexts(self):
    store = _get_metadata_store()
    context_type = _create_example_context_type()
    type_id = store.put_context_type(context_type)
    context_0 = metadata_store_pb2.Context()
    context_0.type_id = type_id
    context_0.name = "context0"
    context_0.properties["bar"].string_value = "Hello"
    context_1 = metadata_store_pb2.Context()
    context_1.name = "context1"
    context_1.type_id = type_id
    context_1.properties["foo"].int_value = -9

    [context_id_0, context_id_1] = store.put_contexts([context_0, context_1])

    context_result = store.get_contexts()
    self.assertLen(context_result, 2)
    self.assertEqual(context_result[0].id, context_id_0)
    self.assertEqual(context_result[0].name, "context0")
    self.assertEqual(context_result[0].properties["bar"].string_value, "Hello")
    self.assertEqual(context_result[1].id, context_id_1)
    self.assertEqual(context_result[1].name, "context1")
    self.assertEqual(context_result[1].properties["foo"].int_value, -9)

  def test_put_contexts_get_contexts_by_type(self):
    store = _get_metadata_store()
    context_type = _create_example_context_type()
    type_id = store.put_context_type(context_type)
    context_type_2 = _create_example_context_type_2()
    type_id_2 = store.put_context_type(context_type_2)
    context_0 = metadata_store_pb2.Context()
    context_0.type_id = type_id
    context_0.name = "context_name"
    context_1 = metadata_store_pb2.Context()
    context_1.type_id = type_id_2
    context_1.name = "context_name"

    [_, context_id_1] = store.put_contexts([context_0, context_1])
    context_result = store.get_contexts_by_type(context_type_2.name)
    self.assertLen(context_result, 1)
    self.assertEqual(context_result[0].id, context_id_1)

  def test_puts_contexts_empty_name(self):
    store = _get_metadata_store()
    with self.assertRaises(errors.InvalidArgumentError):
      context_type = _create_example_context_type()
      type_id = store.put_context_type(context_type)
      context_0 = metadata_store_pb2.Context()
      context_0.type_id = type_id
      store.put_contexts([context_0])

  def test_puts_contexts_duplicated_name_with_the_same_type(self):
    store = _get_metadata_store()
    with self.assertRaises(errors.AlreadyExistsError):
      context_type = _create_example_context_type()
      type_id = store.put_context_type(context_type)
      context_0 = metadata_store_pb2.Context()
      context_0.type_id = type_id
      context_0.name = "the_same_name"
      context_1 = metadata_store_pb2.Context()
      context_1.type_id = type_id
      context_1.name = "the_same_name"
      store.put_contexts([context_0, context_1])

  def test_update_context_get_context(self):
    store = _get_metadata_store()
    context_type = _create_example_context_type()
    type_id = store.put_context_type(context_type)
    context = metadata_store_pb2.Context()
    context.type_id = type_id
    context.name = "context1"
    context.properties["bar"].string_value = "Hello"
    [context_id] = store.put_contexts([context])

    context_2 = metadata_store_pb2.Context()
    context_2.id = context_id
    context_2.name = "context2"
    context_2.type_id = type_id
    context_2.properties["foo"].int_value = 12
    context_2.properties["bar"].string_value = "Goodbye"
    [context_id_2] = store.put_contexts([context_2])
    self.assertEqual(context_id, context_id_2)

    [context_result] = store.get_contexts_by_id([context_id])
    self.assertEqual(context_result.name, context_2.name)
    self.assertEqual(context_result.properties["bar"].string_value, "Goodbye")
    self.assertEqual(context_result.properties["foo"].int_value, 12)

  def test_put_and_use_attributions_and_associations(self):
    store = _get_metadata_store()
    context_type = _create_example_context_type()
    context_type_id = store.put_context_type(context_type)
    want_context = metadata_store_pb2.Context()
    want_context.type_id = context_type_id
    want_context.name = "context"
    [context_id] = store.put_contexts([want_context])
    want_context.id = context_id

    execution_type = _create_example_execution_type()
    execution_type_id = store.put_execution_type(execution_type)
    want_execution = metadata_store_pb2.Execution()
    want_execution.type_id = execution_type_id
    want_execution.properties["foo"].int_value = 3
    [execution_id] = store.put_executions([want_execution])
    want_execution.id = execution_id

    artifact_type = _create_example_artifact_type()
    artifact_type_id = store.put_artifact_type(artifact_type)
    want_artifact = metadata_store_pb2.Artifact()
    want_artifact.type_id = artifact_type_id
    want_artifact.uri = "testuri"
    [artifact_id] = store.put_artifacts([want_artifact])
    want_artifact.id = artifact_id

    # insert attribution and association and test querying the relationship
    attribution = metadata_store_pb2.Attribution()
    attribution.artifact_id = want_artifact.id
    attribution.context_id = want_context.id
    association = metadata_store_pb2.Association()
    association.execution_id = want_execution.id
    association.context_id = want_context.id
    store.put_attributions_and_associations([attribution], [association])

    # test querying the relationship
    got_contexts = store.get_contexts_by_artifact(want_artifact.id)
    self.assertLen(got_contexts, 1)
    self.assertEqual(got_contexts[0].id, want_context.id)
    self.assertEqual(got_contexts[0].name, want_context.name)
    got_arifacts = store.get_artifacts_by_context(want_context.id)
    self.assertLen(got_arifacts, 1)
    self.assertEqual(got_arifacts[0].uri, want_artifact.uri)
    got_executions = store.get_executions_by_context(want_context.id)
    self.assertLen(got_executions, 1)
    self.assertEqual(got_executions[0].properties["foo"],
                     want_execution.properties["foo"])
    got_contexts = store.get_contexts_by_execution(want_execution.id)
    self.assertLen(got_contexts, 1)
    self.assertEqual(got_contexts[0].id, want_context.id)
    self.assertEqual(got_contexts[0].name, want_context.name)

  def test_put_duplicated_attributions_and_empty_associations(self):
    store = _get_metadata_store()
    context_type = _create_example_context_type()
    context_type_id = store.put_context_type(context_type)
    want_context = metadata_store_pb2.Context()
    want_context.type_id = context_type_id
    want_context.name = "context"
    [context_id] = store.put_contexts([want_context])
    want_context.id = context_id

    artifact_type = _create_example_artifact_type()
    artifact_type_id = store.put_artifact_type(artifact_type)
    want_artifact = metadata_store_pb2.Artifact()
    want_artifact.type_id = artifact_type_id
    want_artifact.uri = "testuri"
    [artifact_id] = store.put_artifacts([want_artifact])
    want_artifact.id = artifact_id

    attribution = metadata_store_pb2.Attribution()
    attribution.artifact_id = want_artifact.id
    attribution.context_id = want_context.id
    store.put_attributions_and_associations([attribution, attribution], [])

    got_contexts = store.get_contexts_by_artifact(want_artifact.id)
    self.assertLen(got_contexts, 1)
    self.assertEqual(got_contexts[0].id, want_context.id)
    self.assertEqual(got_contexts[0].name, want_context.name)
    got_arifacts = store.get_artifacts_by_context(want_context.id)
    self.assertLen(got_arifacts, 1)
    self.assertEqual(got_arifacts[0].uri, want_artifact.uri)
    self.assertEmpty(store.get_executions_by_context(want_context.id))

  def test_downgrade_metadata_store(self):
    # create a metadata store and init to the current library version
    connection_config = metadata_store_pb2.ConnectionConfig()
    db_file = os.path.join(absltest.get_default_test_tmpdir(), "test.db")
    connection_config.sqlite.filename_uri = db_file
    metadata_store.MetadataStore(connection_config)

    # wrong downgrade_to_schema_version
    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                "downgrade_to_schema_version not specified"):
      metadata_store.downgrade_schema(connection_config, -1)

    # invalid argument for the downgrade_to_schema_version
    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                "MLMD cannot be downgraded to schema_version"):
      downgrade_to_version = 999999
      metadata_store.downgrade_schema(connection_config, downgrade_to_version)

    # downgrade the metadata store to v0.13.2 where schema version is 0
    metadata_store.downgrade_schema(
        connection_config, downgrade_to_schema_version=0)
    os.remove(db_file)

  def test_enable_metadata_store_upgrade_migration(self):
    # create a metadata store and downgrade to version 0
    db_file = os.path.join(absltest.get_default_test_tmpdir(), "test.db")
    connection_config = metadata_store_pb2.ConnectionConfig()
    connection_config.sqlite.filename_uri = db_file
    metadata_store.MetadataStore(connection_config)
    metadata_store.downgrade_schema(connection_config, 0)

    upgrade_conn_config = metadata_store_pb2.ConnectionConfig()
    upgrade_conn_config.sqlite.filename_uri = db_file
    with self.assertRaisesRegex(RuntimeError, "Schema migration is disabled."):
      # if disabled then the store cannot be used.
      metadata_store.MetadataStore(upgrade_conn_config)

    # if enable, then the store can be created
    metadata_store.MetadataStore(
        upgrade_conn_config, enable_upgrade_migration=True)
    os.remove(db_file)

  def test_error_code_generation(self):
    with self.assertRaises(errors.CancelledError):
      try:
        _create_grpc_error_with_code(grpc.StatusCode.CANCELLED)
      except grpc.RpcError as e:
        raise metadata_store._make_exception(e.details(), e.code().value[0])
    with self.assertRaises(errors.UnknownError):
      try:
        _create_grpc_error_with_code(grpc.StatusCode.UNKNOWN)
      except grpc.RpcError as e:
        raise metadata_store._make_exception(e.details(), e.code().value[0])
    with self.assertRaises(errors.InvalidArgumentError):
      try:
        _create_grpc_error_with_code(grpc.StatusCode.INVALID_ARGUMENT)
      except grpc.RpcError as e:
        raise metadata_store._make_exception(e.details(), e.code().value[0])
    with self.assertRaises(errors.DeadlineExceededError):
      try:
        _create_grpc_error_with_code(grpc.StatusCode.DEADLINE_EXCEEDED)
      except grpc.RpcError as e:
        raise metadata_store._make_exception(e.details(), e.code().value[0])
    with self.assertRaises(errors.NotFoundError):
      try:
        _create_grpc_error_with_code(grpc.StatusCode.NOT_FOUND)
      except grpc.RpcError as e:
        raise metadata_store._make_exception(e.details(), e.code().value[0])
    with self.assertRaises(errors.AlreadyExistsError):
      try:
        _create_grpc_error_with_code(grpc.StatusCode.ALREADY_EXISTS)
      except grpc.RpcError as e:
        raise metadata_store._make_exception(e.details(), e.code().value[0])
    with self.assertRaises(errors.PermissionDeniedError):
      try:
        _create_grpc_error_with_code(grpc.StatusCode.PERMISSION_DENIED)
      except grpc.RpcError as e:
        raise metadata_store._make_exception(e.details(), e.code().value[0])
    with self.assertRaises(errors.UnauthenticatedError):
      try:
        _create_grpc_error_with_code(grpc.StatusCode.UNAUTHENTICATED)
      except grpc.RpcError as e:
        raise metadata_store._make_exception(e.details(), e.code().value[0])
    with self.assertRaises(errors.ResourceExhaustedError):
      try:
        _create_grpc_error_with_code(grpc.StatusCode.RESOURCE_EXHAUSTED)
      except grpc.RpcError as e:
        raise metadata_store._make_exception(e.details(), e.code().value[0])
    with self.assertRaises(errors.FailedPreconditionError):
      try:
        _create_grpc_error_with_code(grpc.StatusCode.FAILED_PRECONDITION)
      except grpc.RpcError as e:
        raise metadata_store._make_exception(e.details(), e.code().value[0])
    with self.assertRaises(errors.AbortedError):
      try:
        _create_grpc_error_with_code(grpc.StatusCode.ABORTED)
      except grpc.RpcError as e:
        raise metadata_store._make_exception(e.details(), e.code().value[0])
    with self.assertRaises(errors.OutOfRangeError):
      try:
        _create_grpc_error_with_code(grpc.StatusCode.OUT_OF_RANGE)
      except grpc.RpcError as e:
        raise metadata_store._make_exception(e.details(), e.code().value[0])
    with self.assertRaises(errors.UnimplementedError):
      try:
        _create_grpc_error_with_code(grpc.StatusCode.UNIMPLEMENTED)
      except grpc.RpcError as e:
        raise metadata_store._make_exception(e.details(), e.code().value[0])
    with self.assertRaises(errors.InternalError):
      try:
        _create_grpc_error_with_code(grpc.StatusCode.INTERNAL)
      except grpc.RpcError as e:
        raise metadata_store._make_exception(e.details(), e.code().value[0])
    with self.assertRaises(errors.UnavailableError):
      try:
        _create_grpc_error_with_code(grpc.StatusCode.UNAVAILABLE)
      except grpc.RpcError as e:
        raise metadata_store._make_exception(e.details(), e.code().value[0])
    with self.assertRaises(errors.DataLossError):
      try:
        _create_grpc_error_with_code(grpc.StatusCode.DATA_LOSS)
      except grpc.RpcError as e:
        raise metadata_store._make_exception(e.details(), e.code().value[0])


if __name__ == "__main__":
  absltest.main()
